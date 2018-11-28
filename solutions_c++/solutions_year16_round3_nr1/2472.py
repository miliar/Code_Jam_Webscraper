#include <bits/stdc++.h>
using namespace std;
#define vi vector < int >
#define pii pair < int , int >
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define foreach(it,v) for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define dbg(x) { cout<< #x << ": " << (x) << endl; }
#define dbg2(x,y) { cout<< #x << ": " << (x) << " , " << #y << ": " << (y) << endl; }
#define all(x) x.begin(),x.end()
#define mset(x,v) memset(x, v, sizeof(x))
#define sz(x) (int)x.size()
#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)

ll gcd(ll a, ll b) {if (a == 0 || b == 0) return max(a,b); if (b % a == 0) return a; return gcd(b%a, a);}
ll hcf(ll a, ll b) {if(b>a) return (hcf(b, a)); if(a%b==0) return b; return (hcf(b, a%b));}
ll modpow(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
ll mulmod(ll a, ll b, ll m) {int64_t res = 0;while (a != 0){if(a & 1)res =(res+b)%m;a>>=1;b =(b<<1)%m;}return res;}

vector<pair<int,char> > a;
int main()
{
	int t,n,test,i,x;
	s(test);
	for(t=1;t<=test;t++)
	{
		a.clear();
		s(n);
		for(i=0;i<n;i++)
		{
			s(x);
			a.pb(mp(x,'A'+i));
		}
		printf("Case #%d: ",t);
		while(a.size())
		{
		sort(a.begin(),a.end(),greater<pair<int,char> >());
		if(a.size()>=2 && a[0].first > 1)
		{
		a[0].first=a[0].first-1;
		a[1].first=a[1].first-1;
		printf("%c%c ",a[0].second,a[1].second);
		if(a[1].first == 0)
		a.erase(a.begin()+1);
		}
		else if(a[0].first==1)
		{
		if(a.size()>2)
		{
		printf("%c ",a[0].second);
		a[0].first=a[0].first-1;
		a.erase(a.begin());
		}
		else if(a.size()==2)
		{
		printf("%c%c ",a[0].second,a[1].second);
		a.erase(a.begin());
		a.erase(a.begin());
		}
		else
		{
		}

		}
		}
		printf("\n");
	}
	return 0;
}
