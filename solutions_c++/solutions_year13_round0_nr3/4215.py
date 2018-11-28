#include<cstdio>
#define ll long long
#define lim 10000000
int T,cs,k;ll a,b,i,j,v[1000000];
int f(ll n)
{
    for(i=0;i<k && v[i]<=n;i++);
    return i;
}
bool pal(ll n)
{
    int i,j,d[20];
    for(i=0;n;n/=10,i++)d[i]=n%10;
    for(j=0,i--;j<i && d[i]==d[j];j++,i--);
    return j>=i;
}
int main()
{
        int ans;
    freopen("fair.txt","r",stdin);
    freopen("fairans.txt","w",stdout);
    for(i=1,k=0;i<=lim;i++)
    {
        if(pal(i) && pal(i*i))v[k++]=i*i;
    }
    //for(i=0;i<k;i++)printf("%lld ",v[i]);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lld %lld",&a,&b);
        ans=f(b)-f(a-1);
        printf("Case #%d: %d\n",++cs,ans);
    }
    return 0;
}

