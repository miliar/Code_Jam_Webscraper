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
    //freopen("inp.txt","r",stdin);
  //  freopen("out.txt","w",stdout);

 ll t,ans,i,l,j,q=1;
 s1(t);
 while(t--)
 {

     ans=0;
     string s;
     cin>>s;
     l=s.length();
     for(i=0;i<l-1;i++)
     {
         if(s[i]==s[i+1])
            continue;
         else
         {
             for(j=0;j<i;j++)
             {
                 if(s[i]=='+')
                    s[i]='-';
                 else
                    s[i]='+';
             }
             ans++;
         }
     }
     if(s[l-1]=='-')
     {
         ans++;
     }
     cout<<"Case #"<<q++<<": "<<ans<<endl;
 }
return 0;
}
