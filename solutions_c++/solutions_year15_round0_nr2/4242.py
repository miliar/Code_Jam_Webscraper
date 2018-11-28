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

#define maxn 10000
ll a[maxn];
int main()
{
	ll t,cas=0,maxi,i,j,n,ans,cnt,maxx,q=1;
	s1(t);
	while(t--)
	{
		maxi=0;
		s1(n);
		for(i=1;i<=n;i++)
		{
			s1(a[i]);
			maxi=max(maxi,a[i]);
		}
		ans=maxi;
		for(i=1;i<=maxi;i++)
		{
			cnt=0;
			maxx=0;
			for(j=1;j<=n;j++)
			{
				if(a[j]>i)
				{
					cnt += (a[j] / i)+((a[j]%i==0)?0:1)-1;
					maxx=max(maxx,i);
				}
				else maxx=max(maxx,a[j]);
			}
			cnt+=maxx;
			if(cnt<ans)ans=cnt;
		}
		cout<<"Case #"<<q++<<": "<<ans<<endl;
	}
	return 0;
}
