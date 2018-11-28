#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define sl(n) scanf("%lld", &n)
#define si(n) scanf("%d", &n)
#define ss(n) scanf("%s", n); getchar();

int main ()
{
   // freopen("B-large.in", "r", stdin);
   // freopen("output.txt", "w", stdout);


    char s[1000], pls;
    ll cs, t, i, j, k, n, x, y, ans, q, cn;

    sl(t);

    for (cs = 1; cs <= t; cs++)
    {
        cn = 0;

        scanf(" %s", s);

        pls = 0;

        for (i = 0; s[i] != 0; i++)
        {
            if (pls == 0)
            {
                pls = s[i];
            }

            if (s[i] == pls)
                continue;
            else
            {
               cn++;
               pls = s[i];
            }
        }

        if (pls == '-')
            cn++;

        printf("Case #%lld: %lld\n", cs, cn);
    }

    return 0;
}
