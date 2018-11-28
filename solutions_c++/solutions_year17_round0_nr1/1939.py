/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define MAXN 100005
#define INF LLONG_MAX
#define mod 1000000007
using namespace std;

ll t, k;
string st;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	F(cas,1,t)
	{
		cin>>st;
		cin>>k;
		ll len = st.length();
		bool flag = 1;
		ll ans = 0;
		F(i,0,len-1)
		{
			if(st[i]=='-')
			{
				ans++;
				if(i+k-1 >= len)
				{
					flag=0;
					break;
				}
				F(j,i,i+k-1)
				{
					if(st[j]=='-')
						st[j]='+';
					else
						st[j]='-';
				}
			}
		}
		cout<<"Case #"<<cas<<": ";
		if(flag)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}    
	return 0;
}