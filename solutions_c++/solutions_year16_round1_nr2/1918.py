#include <bits/stdc++.h>
using namespace std;
#define ReadFile freopen("I:/CODE/B-large.in","r",stdin)
#define Boost ios_base::sync_with_stdio(false)
#define setP(s,p) fixed<<setprecision(p)<<ssss
#define pb emplace_back
#define MOD 1000000007
#define MAX 100010
#define INF LONG_MAX
#define f first
#define s second
#define endl '\n'

typedef long long int ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

map<ll,ll> mp;

int main()
{
	ReadFile;
	Boost;
	ll t,n,a;
	cin>>t;
	for(ll l=1;l<=t;l++)
	{
		mp.clear();
		cin>>n;
		cout<<"Case #"<<l<<": ";
		for(ll i=1;i<=(2*n-1);i++)
		{
			for(ll j=1;j<=n;j++)
			{
				cin>>a;
				mp[a]++;
			}
		}
		for(auto itr=mp.begin();itr!=mp.end();itr++)
		{
			if((itr->s)%2==1)cout<<itr->f<<" ";
		}
		cout<<endl;
	}

	return 0;
}

