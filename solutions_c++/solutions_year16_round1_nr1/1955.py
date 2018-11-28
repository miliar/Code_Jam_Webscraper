#include <bits/stdc++.h>
using namespace std;
#define ReadFile freopen("I:/CODE/A-large.in","r",stdin)
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

int main()
{
	ReadFile;
	Boost;
	ll t,sz;
	cin>>t;
	string s;
	string ans;
	char leftmost;
	for(int l=1;l<=t;l++)
	{
		cin>>s;
		ans="";
		leftmost=s[0];
		ans=ans+s[0];
		sz=s.size();
		cout<<"Case #"<<l<<": ";
		for(ll i=1;i<sz;i++)
		{
			if(s[i]>=leftmost)
			{
				ans=s[i]+ans;
				leftmost=s[i];
			}
			else
			{
				ans=ans+s[i];
			}
		}
		cout<<ans<<endl;
	}

	return 0;
}

