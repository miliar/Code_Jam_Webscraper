#include <bits/stdc++.h>
using namespace std;

typedef long long int64;

const int mult[5][5] = {{0, 0, 0, 0, 0},
                        {0, 1, 2, 3, 4}, 
                        {0, 2, -1, 4, -3},
                        {0, 3, -4, -1, 2},
                        {0, 4, 3, -2, -1}};

const int bias = 4;

int get_id(char c) {
    if (c == 'i')
        return 2;
    if (c == 'j')
        return 3;
    if (c == 'k')
        return 4;
}

int mul(int i, int j) {
    int sign = 1;
    if (i < 0) {
        sign = -sign;
        i = -i;
    }
    if (j < 0) {
        sign = -sign;
        j = -j;
    }
    return sign * mult[i][j];
}

int nTest;
int l, x;
char s[10010];

int gone[10010][10];
int next(int i, int value, int req_value, int req_position = -1) {
    memset(gone, 0, sizeof gone);

    while (true) {
        if (value == req_value) 
            if (req_position == -1 || (i - 1 + l) % l == req_position)
                return i - 1;
        if (gone[i % l][value + bias])
            return -1;
        gone[i % l][value + bias]++;
        value = mul(value, s[i % l]);
        i++;
    }
}

bool check_ending(int64 remain) {
    if (remain == 0) 
        return true;

    memset(gone, 0, sizeof gone);
    for (int i = 0, value = 1; i < remain; i++) {
        if (gone[i % l][value + bias])
            return false;
        gone[i % l][value + bias]++;
        value = mul(value, s[i % l]);
        if (value == 1) {
            if (remain % (i + 1) == 0 && (i + 1) % l == 0)
                return true;
        }
    }
    return false;
}

int main() {

    freopen("C-small-attempt2.in", "r", stdin);
    // freopen("C.txt", "r", stdin);
    freopen("C_out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {
        scanf("%d%d", &l, &x);
        scanf("%s", s);

        for (int i = 0; i < l; i++)
            s[i] = get_id(s[i]);

        int p_i = next(0, 1, 2);
        if (p_i != -1 && p_i < int64(l) * x) {
            int p_j = next(p_i + 1, 1, 3);
            if (p_j != -1 && p_j < int64(l) * x) {
                int p_k = next(p_j + 1, 1, 4, l - 1);
                if (p_k != -1 && p_k < int64(l) * x) {
                    int64 remain = int64(l) * x - 1 - p_k;
                    if (check_ending(remain)) 
                        printf("Case #%d: YES\n", test);
                    else 
                        printf("Case #%d: NO\n", test);
                } else 
                    printf("Case #%d: NO\n", test);
            } else
                printf("Case #%d: NO\n", test);
        } else 
            printf("Case #%d: NO\n", test);

    }

    return 0;
}