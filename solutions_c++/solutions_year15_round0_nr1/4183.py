#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
#define pb(f) push_back(f)
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define pi(c) printf("%d\n",c)
#define pil(c) printf("%lld\n",c)
#define ll long long int
#define pii pair<int,int>
#define vi vector<int>
#define scs(a) scanf("%s",a)
using namespace std;
#define mod 1000000007
char s[1004];
int a[1004];
int main()
{
	int t;
	sc(t);
	int caase=1;
	while(t--)
	{
		int n,i,j,k;
		sc(n);
		scs(s);
		for(i=0;i<=n;i++)
		{
			a[i]=s[i]-'0';
		//	p%d i(a[i]);
		}
		ll ans=0,cnt=0;
		for(i=0;i<=n;i++)
		{
			if(cnt>=i)
			{
				cnt+=a[i];
			}
			else
			{
				//cout<<"ans "<<ans<<" i "<<i<<endl;
				ans+=i-cnt;
				cnt=i;
				//cout<<"ans "<<ans<<" i "<<i<<endl;
				cnt+=a[i];
			}
		}
		printf("Case #%d: %lld\n",caase,ans);
		caase++;
	}
}

