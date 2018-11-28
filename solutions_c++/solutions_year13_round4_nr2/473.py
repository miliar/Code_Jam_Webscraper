#include <cstdio>
typedef long long ll;
ll calc(int n,ll p)
{
    ll m=1LL<<n;
    if (p==m)
        return(m-1);
    ll ans=0,k=2;
    while (p)
    {
        if (p<=m/2)
            return(ans);
        p-=m/2;
        m/=2;
        ans+=k;
        k<<=1;
    }
}
ll rev_calc(int n,ll p)
{
    ll m=1LL<<n;
    if (p==m)
        return(m-1);
    ll ans=calc(n,m-p);
    return(m-ans-2);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n;
        ll p;
        scanf("%d%lld",&n,&p);
        static int id=0;
        printf("Case #%d: %lld %lld\n",++id,calc(n,p),rev_calc(n,p));
    }
    return(0);
}

