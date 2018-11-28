/*input
3
---+-++- 7
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define F(i,a,b) for(ll i = a; i <= b; i++)
#define RF(i,a,b) for(ll i = a; i >= b; i--)
#define pii pair<ll,ll>
#define PI 3.14159265358979323846264338327950288
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define P(x) printf("%d\n",x)
#define all(v) v.begin(),v.end()
int main() 
{
	std::ios::sync_with_stdio(false);
	freopen("is1.txt","r",stdin);
	freopen("os1.txt","w",stdout);
	ll tc=1;
	ll t;
	cin>>t;
	//S(t);
	while(t--)
	{
		cout<<"Case #"<<tc++<<": ";
		string s;
		cin>>s;
		ll k;
		cin>>k;
		ll n = s.length();
		ll ans = 0;
		F(i,0,n-1)
		{
			if(s[i]=='+')
				continue;
			if(i+k-1 > n-1)
				continue;
			ans++;
			F(j,i,i+k-1)
			{
				if(s[j]=='-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
		F(i,0,n-1)
		{
			if(s[i]=='-')
				ans = -1;
		}
		if(ans == -1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}