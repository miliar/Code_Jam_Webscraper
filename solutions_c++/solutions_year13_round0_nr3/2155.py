#include <cstdio>
#include <cstdlib>
#include <cstring>
long long n,m,p[15]; int t;
long long log(long long x)
{
    for(int i=0;i<15;++i) if(p[i]<=x&&p[i+1]>x) return i;
}
bool check(long long x)
{
    long long len=log(x);
    for(int i=0;i<=len;++i) if(x%p[i+1]/p[i]!=x%p[len-i+1]/p[len-i]) return 0;
    return 1;
}
long long calc(long long x)
{
    long long c=0;
    for(long long i=1;i*i<=x;++i) if(check(i)&&check(i*i)) ++c;
    return c;
}
int main()
{
    freopen("in3","r",stdin);
    freopen("out3","w",stdout);
    scanf("%d",&t);
    p[0]=1; for(int i=1;i<15;++i) p[i]=p[i-1]*10;
    for(int I=1;I<=t;++I)
    {
        scanf("%lld%lld",&n,&m);
        printf("Case #%d: %lld\n",I,calc(m)-calc(n-1));
    }
    return 0;
}
