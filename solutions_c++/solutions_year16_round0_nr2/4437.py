/*input
5
-
-+
+-
+++
--+-
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define inf LLONG_MAX
#define mod 1000000007
#define MAXN 100005
#define pb(x) push_back(x)

ll t, len, cnt;
string s;
char ch;

int main() 
{
	freopen("inp2.in","r",stdin);
	freopen("out2.txt","w",stdout);
	cin>>t;
	F(count,1,t)
	{
		cout<<"Case #"<<count<<": ";
		cnt=0;
		cin>>s;
		len=s.length();
		ch=s[0];
		F(i,1,len-1)
		{
			if(s[i]!=ch)
			{
				cnt++;
				ch=s[i];
			}
		}
		if(ch=='-')
			cnt++;
		cout<<cnt<<endl;
	}	
	return 0;
}