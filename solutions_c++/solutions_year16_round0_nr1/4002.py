// In the name of GOD
// A fan of Michal Danilak a.k.a Mimino
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vi vector<int>
#define piii pair < int,pair <int,int> >
#define f first
#define s second
#define MOD 1000000007
#define MAX 5000000
#define IOS ios_base::sync_with_stdio(0)
#define PI 3.1415926535897932384626
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
bool  isone(ll,int);
int count(ll);
ll exp(ll,ll,ll);
ll GCD(ll,ll);
int main()
{
	IOS;
	#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
    freopen("QR_A_lout.txt", "w", stdout);
	#endif
	int n;cin>>n;
	for(int tc=1;tc<=n;tc++)
	{
		int x;cin>>x;
		int vis[10]={0};
		int cnt=0;
		for(int i=1;i<=MAX;i++)
		{
			
			ll y=x*1LL*i;
			ll t=y;
			while(y)
			{
				if(!vis[y%10LL])
				{
					cnt++;
					vis[y%10LL]=1;
				}
				y/=10LL;
			}
			if(cnt==10)
			{
				cout<<"Case #"<<tc<<": "<<t<<"\n";
				break;
			}
		}
		if(cnt!=10)
			cout<<"Case #"<<tc<<": INSOMNIA\n";
	}
	return 0;
}

ll GCD(ll a,ll b)
{
   if(!b) return a;
   else   return GCD(b,a%b);
}
ll exp(ll a,ll b,ll c)
{
	ll ret=1LL;
	ll mult=a;
	while(b)
	{
		if(b&1)	ret=(ret*mult)%c;
		mult=(mult*mult)%c;
		b>>=1;
	}
	return ret;
}
int count(ll x)
{
   int ret=0;
   while(x)
   {
		   if(x&1)  ret++;
		   x>>=1LL;
   }
   return ret;
}

bool isone(ll x,int pos)
{
	 return x&(1<<pos);
}





