#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define For(i,a,b) for(int i=a-1;i>=b;i--)
#define rep(i,b) FOR(i,0,b)
#define Rep(i,b) For(i,a,0)
#define SORT(x) sort(x.begin(),x.end());
#define ERASE(x) x.erase(x.begin(),x.end());
#define FILL(x,i) memset(x,i,sizeof(x));
#define K 1000000007
#define L 400
#define s1(a) scanf("%d",&a);
#define s2(a) scanf("%lld",&a);
#define s3(a,b) scanf("%lld%lld",&a,&b);
#define s4(a,b,c) scanf("%lld%lld%lld",&a,&b,&c);
#define pb push_back
#define mp make_pair
#define F first
#define S second 
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define EPS 0.000001
#define MAX 1

typedef long long int ll;

bool cmp(ll a,ll b){if(a>b) return true; return false;}

ll powr(int s,int p)
{
	if(p==0)
		return 1;	
 
	if(p%2==1)
	{
		ll q=powr(s,p/2);
		ll a=q;
		q=(a*a);
		q=(q*s);	
		return ( q );
	}
 
	else
	{
		ll q=powr(s,p/2);
		ll a=q;
		q=(a*a);	
		return (q);
	}
}
/*******************************MAIN CODE STARTS*******************************/

ll t,n,h[10],add;

int main()
{
	int t=1;
	s1(t)
	FOR(i,1,t+1)
	{
		printf("Case #%d: ",i);
		s2(n)
		if(n==0)
			cout<<"INSOMNIA\n";
		else
		{
			add = n;
			FILL(h,0)
			int flag=1;
			while(true)
			{
				ll b=n;
				while(b)
				{
					int a = b%10;
					b = b/10;
					h[a]=1;
					//cout<<a<<'\n';
				}
				FOR(i,0,10)
				{
					if(h[i]==0)
						flag=0;
				}
				if(flag)
					break;
				flag=1;
				n += add;
			}
			cout<<n<<'\n';
		}
	}
	return 0;
}
