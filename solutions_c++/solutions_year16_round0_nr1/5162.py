#include <bits/stdc++.h>

#define sd(x)       scanf("%d", &x)
#define slld(x)     scanf("%lld", &x)
#define sc(x)       scanf("%c", &x)
#define pd(x)       printf("%d", x)
#define plld(x)     printf("%lld\n", x)
#define pc(x)       printf("%c", x)
#define pdln(x)     printf("%d\n", x)
#define prl(x)      cout << x << endl
#define LL          long long
#define forn(i, n)  for(int i = 0; i < (int)n; i++)
#define fori(i, n)  for(int i = 1; i <= (int)n; i++)
#define revn(i, n)  for(int i = (int)(n - 1); i >= 0; i--)
#define pb          push_back
#define pii         pair <int, int>

#define mem(x, y)   memset(x, y, sizeof(x))
#define MAX         100002
#define MOD         1000000007

using namespace std;

bool d[10];
int n, m, r, cnt, p;


int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("large.out", "w", stdout);
    int test, caseno;
    sd(test);
    for(caseno = 1; caseno <= test; caseno++)
    {
        mem(d, 0);
        sd(n);
        cnt = 0;
        int f = 0;
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", caseno);
            continue;
        }
        for(int i = 1; i <= 100; i++)
        {
            p = m = n * i;
            while(m)
            {
                r = m % 10;
                m = m / 10;
                if(!d[r])
                {
                    d[r] = 1;
                    cnt++;
                }
            }
            if(cnt >= 10)
            {
                f = 1;
                break;
            }
        }
        if(f) printf("Case #%d: %d\n", caseno, p);
        else printf("Case #%d: INSOMNIA\n", caseno);
    }
    return 0;
}

