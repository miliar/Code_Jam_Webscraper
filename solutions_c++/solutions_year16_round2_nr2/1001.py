#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxN = 20;

int n;
char s1[maxN], s2[maxN];
ll p[maxN];
ll res1, res2;

void Build(int i, ll num1, ll num2) {
    if (i == 0) {
        if (abs(num1 - num2) < abs(res1 - res2)) {
            res1 = num1; res2 = num2;
        }
        else
        if (abs(num1 - num2) == abs(res1 - res2)) {
            if (num1 < res1) {
                res1 = num1; res2 = num2;
            }
            else
            if (num1 == res1) {
                if (num2 < res2) {
                    res1 = num1; res2 = num2;
                }
            }
        }
        return;
    }

    if (s1[i] != '?' && s2[i] != '?') {
        Build(i - 1, num1 + (s1[i] - '0') * p[i], num2 + (s2[i] - '0') * p[i]);
        return;
    }
    if (s1[i] == '?' && s2[i] == '?') {
        /*Build(i - 1, num1, num2);
        Build(i - 1, num1 + 9 * p[i], num2);
        Build(i - 1, num1, num2 + 9 * p[i]);
        Build(i - 1, num1 + 1 * p[i], num2);
        Build(i - 1, num1, num2 + 1 * p[i]);*/
        for(int c1 = 0; c1 <= 9; ++c1)
            for(int c2 = 0; c2 <= 9; ++c2)
                Build(i - 1, num1 + c1 * p[i], num2 + c2 * p[i]);
        return;
    }
    if (s1[i] != '?') {
        /*Build(i - 1, num1 + (s1[i] - '0') * p[i], num2);
        Build(i - 1, num1 + (s1[i] - '0') * p[i], num2 + (s1[i] - '0') * p[i]);
        Build(i - 1, num1 + (s1[i] - '0') * p[i], num2 + 9 * p[i]);
        Build(i - 1, num1 + (s1[i] - '0') * p[i], num2 + 1 * p[i]);*/
        for(int c2 = 0; c2 <= 9; ++c2)
            Build(i - 1, num1 + (s1[i] - '0') * p[i], num2 + c2 * p[i]);
        return;
    }

    /*Build(i - 1, num1, num2 + (s2[i] - '0') * p[i]);
    Build(i - 1, num1 + (s2[i] - '0') * p[i], num2 + (s2[i] - '0') * p[i]);
    Build(i - 1, num1 + 9 * p[i], num2 + (s2[i] - '0') * p[i]);
    Build(i - 1, num1 + 1 * p[i], num2 + (s2[i] - '0') * p[i]);*/
    for(int c2 = 0; c2 <= 9; ++c2)
        Build(i - 1, num1 + c2 * p[i], num2 + (s2[i] - '0') * p[i]);
}

void Print(ll res, int len) {
    int ch[len];
    memset(ch, 0, sizeof ch);
    int cnt = 0;
    do {
        ch[cnt++] = res % 10;
        res /= 10;
    } while (res > 0);

    for(int i = len - 1; i >= 0; --i) printf("%d", ch[i]);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d\n", &nTests);
    for(int t = 1; t <= nTests; ++t) {
        printf("Case #%d: ", t);
        scanf("%s %s\n", s1 + 1, s2 + 1);
        int n = strlen(s1 + 1);
        p[n] = 1;
        for(int i = n - 1; i >= 1; --i) p[i] = p[i+1] * 10ll;
        res1 = -1e18; res2 = 1e18;
        Build(n, 0, 0);

        Print(res1, n);
        printf(" ");
        Print(res2, n);
        printf("\n");
    }

    return 0;
}
