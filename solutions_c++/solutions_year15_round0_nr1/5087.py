/*
ID: Loeabc123456@gmail.com
LANG: C++
*/
#include <iostream>
#include <cstdio>
using namespace std;
int main ()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    char s[1200];
    int tot, n;
    int tt = 0, ans = 0;
    scanf("%d", &tot);
    for (int ii = 1; ii <= tot; ii++)
    {
        tt = 0; ans = 0;
        scanf("%d%s", &n, s);
        for (int i = 0; i <= n; i++)
        {
            if (tt >= i) tt = tt + s[i] - '0';
            else
            {
                ans += i - tt;
                tt = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", ii, ans);
    }
    return 0;
}
