#include<cstdio>
#include<cmath>
typedef long long LL;
int main()
{
    int t,n;
    LL p, a1, a2;
    freopen("bl.in","r",stdin);
    freopen("bl.out","w",stdout);
    scanf("%d",&t);
    for(int cnt=1;cnt<=t;cnt++)
    {
        scanf("%d%lld",&n,&p);
        if(p == (1ll<<n))
            a1 = a2 = p - 1;
        else
        {
            a1 = 0;
            LL d = 1ll<<(n - 1), b = 2;
            LL pp = d;
            while(pp < p)
            {
                d >>= 1;
                a1 += b;
                b <<= 1;
                pp += d;
            }
            a2 = 1ll<<n;
            d = 1ll<<(n+1);
            while(p)
            {
                p>>=1;
                d>>=1;
            }
            a2 -= d;
        }
        printf("Case #%d: %lld %lld\n",cnt,a1,a2);
    }
    return 0;
}
