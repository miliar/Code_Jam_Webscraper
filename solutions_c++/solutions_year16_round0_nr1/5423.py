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
//freopen("out.txt","w",stdout);

 ll t,n,i,j,cnt=0,cnt1,d,x,q,ans;
    s1(t);
    while(t--)
    {
        cnt++;
        s1(n);
        ll ar[10]={0};
        if(n==0)
            cout<<"Case #"<<cnt<<": "<<"INSOMNIA"<<endl;
        else
        {
            cnt1=0;
            q=1;
            while(cnt1<10)
            {
                d=q*n;
                q++;
                ans=d;
                while(d)
                {
                    x=d%10;
                    if(ar[x]==0)
                    {
                        cnt1++;
                        ar[x]=1;
                    }
                    d/=10;
                }

            }
            cout<<"Case #"<<cnt<<": "<<ans<<endl;
        }
    }
return 0;
}

