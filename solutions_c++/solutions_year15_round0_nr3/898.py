#include <bits/stdc++.h>
using namespace std;

const int MAXN = 10005;

int mat[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1},
};

char data[MAXN*20];
long long l, x;
int sign(int x)
{
    return x>0?1:-1;
}

int calc(int a, int b)
{
    return sign(a)*mat[abs(a)][abs(b)];
}
bool solve()
{
    int tot = 1;
    for (int i = 0; i < x*l; ++i) {
        tot = calc(tot, data[i]);
    }
    if (tot != -1) {
        return false;
    }
    int a = 1;
    for (int i = 0; i < 4*l && i < x*l; ++i) {
        a = calc(a, data[i]);
        if (a != 2) {
            continue;
        }
        int b = 1;
        for (int j = i+1; j < i+4*l && j < x*l; ++j) {
            b = calc(b, data[j]);
            if (b == 3) {
                return true;
            }
        }
    }
    return false;
}

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> l >> x;
        if (x > 12) {
            x = 12 + x%4;
        }
        cin >> data;
        for (int i = 0; i < l; ++i) {
            data[i] = data[i]-'g';
        }

        for (int i = 1; i < x; ++i) {
            memcpy(data+l*i, data, l*sizeof(char));
        }
        printf("Case #%d: %s\n", t, solve()?"YES":"NO");
    }
    return 0;
}
