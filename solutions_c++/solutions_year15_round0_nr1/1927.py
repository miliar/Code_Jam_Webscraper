#include <bits/stdc++.h>

using namespace std;

char s[2000];
int T, n, ans, res;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("ou.out", "w", stdout);
    scanf("%d", &T);
    for (int itest = 0; itest < T; itest++)
    {
        scanf("%d", &n);
        scanf("%s", &s);
        res = ans = 0;
        for (int i = 0; i <= n; i++)
            if (res < i) ans += i - res, res = i + s[i] - 48;
            else res += s[i] - 48;
        printf("Case #%d: %d\n", itest + 1, ans);
    }
}
