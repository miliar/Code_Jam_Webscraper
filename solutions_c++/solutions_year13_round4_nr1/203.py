#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

struct AA
{
    long long s,fg,p;
}a[2010];
bool cmp(AA a,AA b)
{
    if (a.s==b.s)
    {
        return a.fg<b.fg;
    }
    return a.s<b.s;
}

AA stac[2020];
int N,M;

int main()
{
    long long mod=1000002013;
   // freopen("A-large.in","r",stdin);
  //  freopen("A-large.out","w",stdout);
    int T;
    int cas=1;
    scanf("%d",&T);
    while (T--)
    {
        long long cal=0;
        scanf("%d%d",&N,&M);
        for (int i=0;i<M;i++)
        {
            long long s,e,p;
            scanf("%lld%lld%lld",&s,&e,&p);
            cal+=p*((N+N-e+s+1)*(e-s)/2%mod)%mod;
            cal%=mod;
            a[i*2].s=s;
            a[i*2].fg=0;
            a[i*2].p=p;
            a[i*2+1].s=e;
            a[i*2+1].fg=1;
            a[i*2+1].p=p;
        }
        long long ans=0;
        sort(a,a+2*M,cmp);
        int top=0;
        for (int i=0;i<2*M;i++)
        {
            if (a[i].fg==0)
            {
                stac[top].p=a[i].p;
                stac[top].s=a[i].s;
                top++;
            }
            else
            {
                long long x=a[i].p;
                while (top>0 && stac[top-1].p<x)
                {
                    AA y=stac[--top];
                    ans+=y.p*((N+N-a[i].s+y.s+1)*(a[i].s-y.s)/2%mod);
                    ans%=mod;
                    x-=y.p;
                    //cout<<ans<<' '<<a[i].s<<' '<<y.s<<endl;
                }
                AA y=stac[--top];
                ans+=x*((N+N-a[i].s+y.s+1)*(a[i].s-y.s)/2%mod)%mod;
                ans%=mod;
                y.p-=x;
                stac[top++]=y;
               // cout<<ans<<' '<<a[i].s<<' '<<y.s<<endl;
            }
           // cout<<ans<<endl;
        }
      //  cout<<cal<<' '<<ans<<endl;
        printf("Case #%d: %lld\n",cas++,(cal-ans+mod)%mod);
    }
}
