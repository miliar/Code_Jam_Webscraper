#include<bits/stdc++.h>
using namespace std;

#define s(x) scanf("%d",&x)
#define s1(x) scanf("%lld",&x)
#define p(x) printf("%d\n",x)
#define p1(x) printf("%lld\n",x)
#define ps(x) printf("%d ",x)
#define p1s(x) printf("%lld ",x)
#define st(x) scanf("%s",x)
#define pt(x) printf("%s",x)
#define Y printf("YES\n")
#define N printf("NO\n")
#define mod 1000000007
#define ll long long

ll power(ll b, ll e)
{
    ll p = 1;
    while (e > 0)
    {
       if(e&1)
        {
          p=(p*b)%mod;
        }
        e=e>>1;
        b=(b*b)%mod;
    }
    return p;
}

int main()
{
 ll t,n,j,i,ans1,ans2,cnt,q=1;
 s1(t);
 while(t--)
 {
      s1(n);
      ll m[n];
      for(i=0;i<n;i++)
      {
          s1(m[i]);
      }
      ans1=0;
      ans2=0;
      for(i=0;i<n-1;i++)
      {
        if(m[i]-m[i+1]>0)
        {
            ans1+=m[i]-m[i+1];
        }
        if(m[i]-m[i+1]<=0)
            ans1+=0;
       }
       cnt=m[n-2]-m[n-1];
       for(i=0;i<n-1;i++)
       {
           if(m[i]-m[i+1]>cnt)
           {
               cnt=m[i]-m[i+1];
           }
       }
       for(i=0;i<n-1;i++)
       {
         if(m[i]>cnt)
            ans2+=cnt;
         else
            ans2+=m[i];
        }
        cout<<"Case #"<<q++<<": "<<ans1<<" "<<ans2<<endl;
    }
return 0;
}
