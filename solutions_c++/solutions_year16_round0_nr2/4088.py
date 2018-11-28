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
#define IOS ios_base::sync_with_stdio(0)
#define PI 3.1415926535897932384626
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
bool  isone(ll,int);
int count(ll);
ll exp(ll,ll,ll);
ll GCD(ll,ll);
#define MAXN 10101
int dp[MAXN][2];
int main()
{
	IOS;
	#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
    freopen("QR_B_lout.txt", "w", stdout);
	#endif
	int n;cin>>n;
	for(int tc=1;tc<=n;tc++)
	{
		string a;cin>>a;
		for(int i=0;i<MAXN;i++)
			dp[i][0]=dp[i][1]=MOD;
		dp[0][0]=(a[0]=='-');
		dp[0][1]=1-dp[0][0];
		for(int i=1;i<a.length();i++)
		{
			if(a[i]=='+')
			{
				dp[i][0]=dp[i-1][0];
				dp[i][1]=1+dp[i-1][0];
			}
			else
			{
				dp[i][0]=dp[i-1][1]+1;
				dp[i][1]=dp[i-1][1];
			}
		}
		cout<<"Case #"<<tc<<": "<<dp[a.length()-1][0]<<"\n";
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





