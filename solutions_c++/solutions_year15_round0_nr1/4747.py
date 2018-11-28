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
	ll t,cnt,ans,s,i,q=1;
	s1(t);
	while(t--)
	{
		s1(s);
		char arr[1005];
		cin>>arr;
		ll a[1005];
		for(i=0;i<=s;i++)
		{
			a[i]=arr[i]-48;
		}
        cnt=a[0];
        ans=0;
		for(i=1;i<=s;i++)
		{
			if(a[i]==0)
			continue;
			if(cnt<i)
			{
			ans+=i-cnt;
			cnt+=a[i]+ans;
			}
			else
			cnt+=a[i];
		}
		cout<<"Case #"<<q++<<": "<<ans<<endl;
	}


		return 0;
}
