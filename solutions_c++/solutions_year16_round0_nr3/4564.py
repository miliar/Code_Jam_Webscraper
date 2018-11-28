#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define lim 100005
#define mk make_pair
#define pll pair<ll,ll>
#define pb push_back
#define X first
#define Y second
#define MOD 1000000007
#define ios ios_base::sync_with_stdio(0)


int main(void)
{
	ios;
	ll a,n,b,m,c,d,e,t,j,f;
	bool vis[10*lim];
	freopen("input2.txt","r",stdin);
	freopen("output3.txt","w",stdout);
	vector<ll> v[55],r;
	string s;
	cin>>t;
	cin>>n>>j;
	ll ct=0;
	cout<<"Case #1:\n";
	for(ll mask=0;mask<(1<<n);mask++)
	{
		//memset(vis,0,sizeof(vis));
		if(2*mask>(1<<n) and mask%2==1)
		{
		ll cnt=0;
		//ksdjkjdk
		c=mask;
		while(c>0)
		{
		b=c%2;
		s.pb(b+'0');
		c/=2;
		}
		reverse(s.begin(),s.end());
		for(ll i=2;i<=10;i++)
		{
			m=1;
			cnt=0;
			for(ll k=s.size()-1;k>=0;k--)
			{
				if(s[k]=='1')
				cnt+=m;
				m*=i;
			}
			for(e=2;e*e<=cnt;e++)
			{
			if(cnt%e==0)
			{
				r.pb(e);
				break;
			}
			}
			
		}
		if(r.size()==9)
		{
			cout<<s<<" ";
			for(ll x=0;x<9;x++)
			cout<<r[x]<<" ";
			cout<<endl;
			ct++;
		}
		if(ct==j)
		break;
		r.clear();
		s.clear();
	}
	else
	continue;
	}
	
	return 0;
}
