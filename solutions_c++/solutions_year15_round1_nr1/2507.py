//Caution to the wind,complete freedom
#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
return (ll)ret;
}
using namespace std;
#define pi acos(-1.0)
#define MAXA 1000003
#define sl(n) scanf("%lld",&n)
#define mem(x,a) memset(x,a,sizeof(x))
ll a[10005];
int main()
{
    freopen("input.IN","r",stdin);
    freopen("out.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    int n,t,i,j;
    cin>>t;
   for(i=1;i<=t;i++)
   {
       cin>>n;
       ll ans=0,ans1=0,sum=0;
       for(j=0;j<n;j++)
        cin>>a[j];
        printf("Case #%d: ",i);
       ll mx=-1;
       for(j=1;j<n;j++)
       {
           if(a[j]<=a[j-1])
            ans+=(-a[j]+a[j-1]);
            mx=max(mx,-a[j]+a[j-1]);
       }
       for(j=0;j<n-1;j++)
       {
           if(a[j]<=mx)
           {
               ans1+=a[j];
           }
           else
           {
                  ans1+=mx;

           }
       }

       printf("%lld %lld\n",ans,ans1);
   }

    return 0;
}
