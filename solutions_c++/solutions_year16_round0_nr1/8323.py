#include<bits/stdc++.h>
using namespace std;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define P(a,n) for(int i=a;i<=n;i++) cout<<a[i]<<" "; 
#define bp(n) __builtin_popcount(n);
#define D 1000000007
#define pb push_back
#define ci(x) cin>>x;
#define c2(x,y) cin>>x>>y;
#define c3(x,y,z) cin>>x>>y>>z;
#define p2(x,y) cout<<x<<" "<<y<<endl;
#define p3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl;
#define co(x) cout<<x<<endl;
#define r0 return 0;
#define r1 return 1;
#define fi first
#define se second
#define mp make_pair

typedef vector<int> VI;
typedef long double ld;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> VII;
typedef vector<ll> VL;
typedef vector<pll> VLL;
ll tpp = 9e18; int tp = 1e9;
ll n,t;
VI a;
int main()
{
	_
	ci(t);
	for(int i=0;i<10;i++) a.pb(0);
	for(int i=1;i<=t;i++)	
	{
		ci(n);
		if(n==0) 
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		ll temp,cnt=0;
		for(int j=0;j<10;j++) a[j]=0;
		for(ll j=n;;j+=n)
		{
			temp=j;
			while(temp>0)
			{
				ll dig = temp%10;
				if(a[dig]!=1)
				{
					a[dig]=1;
					cnt++;
				}
				temp /= 10;
			}
			if(cnt==10)
			{
				cout<<"Case #"<<i<<": "<<j<<endl;
				break;
			}
		}
	}
	r0;
}

