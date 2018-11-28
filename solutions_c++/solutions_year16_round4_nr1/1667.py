/*input
1
3 3 3 2
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

ll t, r, p, s, n;
map < string, string > mp;
string ans;

void pre()
{
	mp["P"]="PR";
	mp["S"]="PS";
	mp["R"]="RS";
}

string func(string ch, ll n)
{
	ll len;
	string st="";
	st+=ch;
	F(i,2,n)
	{
		string tmp="";
		len=st.length();
		string t1, t2;
		t1=t2="";
		F(j,0,len/2-1)
			t1=t1+st[j];
		F(j,len/2,len-1)
			t2=t2+st[j];
		if(mp[t1].compare(mp[t2])<0)
			tmp=mp[t1]+mp[t2];
		else
			tmp=mp[t2]+mp[t1];
		mp[st]=tmp;
		st=tmp;
	}
	return st;
}

bool valid()
{
	ll R, P, S;
	R=P=S=0;
	ll len=ans.length();
	F(i,0,len-1)
	{
		if(ans[i]=='R')
			R++;
		if(ans[i]=='P')
			P++;
		if(ans[i]=='S')
			S++;
	}
	return R==r && P==p && S==s;
}

int main() 
{
	freopen("inp.in","r",stdin);
	freopen("out.txt","w",stdout);
	pre();
	cin>>t;
	F(count,1,t)
	{
		cout<<"Case #"<<count<<": ";
		cin>>n>>r>>p>>s;
		ans=func("PR", n);
		if(valid())
			cout<<ans<<endl;
		else
		{
			ans=func("PS", n);
			if(valid())
				cout<<ans<<endl;
			else
			{
				ans=func("RS", n);
				if(valid())
					cout<<ans<<endl;
				else
				{
					cout<<"IMPOSSIBLE"<<endl;
				}
			}
		}
	}	
	return 0;
}