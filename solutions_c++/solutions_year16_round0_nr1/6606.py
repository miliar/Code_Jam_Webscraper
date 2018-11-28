#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define sl(n) scanf("%lld", &n)
#define si(n) scanf("%d", &n)
#define ss(n) scanf("%s", n); getchar();

int main ()
{
  //  freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);

    ll cs, t, i, j, k, n, x, y, ans, q, flag[10], nn, temp, mx = 0;

    sl(t);

    for (cs = 1; cs <= t; cs++)
    {
        for (i = 0; i < 10; i++)
            flag[i] = 0;

        sl(n);

        if (n == 0)
        {
            printf("Case #%lld: INSOMNIA\n", cs);
            continue;
        }

        for (j = 1; ; j++)
        {
            nn = j*n;

            temp = nn;

            while (temp != 0)
            {
                flag[temp%10] = 1;
                temp /= 10;
            }

            for (i = 0; i < 10; i++)
            {
                //    printf("%lld %lld %lld\n", nn, i, flag[i]);
                if (flag[i] == 0)
                    break;
            }

            if (i == 10)
                break;
        }

        if (j > mx)
            mx = j;

        printf("Case #%lld: %lld\n", cs, nn);

    }

    return 0;
}
