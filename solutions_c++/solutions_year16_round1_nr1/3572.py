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
int t;
string s;
char a[2004];
int main()
{
	_
	ci(t);
	for(int j=1;j<=t;j++)
	{
		ci(s);
		a[1000] = s[0];
		char temp = s[0];
		int px = 1000,py = 1000;
		for(int i=1;i<s.length();i++)
		{	
			if((int)(s[i] - 'A') >= (int)(temp - 'A'))
			{
				px--;
				a[px] = (char)s[i];
				temp = a[px];
			}
			else
			{
				py++;
				a[py] = (char)s[i];
			}
		}
		cout<<"Case #"<<j<<": ";
		for(int i=px;i<=py;i++) 
			cout<<a[i];
		cout<<endl;
	}
	r0;
}
	
