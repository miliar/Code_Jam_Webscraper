#include <bits/stdc++.h>
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define mp make_pair
#define pb push_back 
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sortv(a) sort(a.begin(),a.end())
#define test()  int t; cin>>t; while(t--)
#define fi first
#define se second
#define el "\n"
#define ll long long
#define ull unsigned ll
#define TRACE
using namespace std;

FILE *fin = freopen("input.txt","r",stdin);
FILE *fout = freopen("output.txt","w",stdout);

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;

#define MAXN 1000009
ll ans[MAXN];
int a[10];
bool check(int val)
{
	while(val)
	{
		a[val%10]++;
		val/=10;
	}	
	rep(i,10)
	{
		if(a[i]==0)
			return false; 
	}
	return true;
}
int main()
{
	ios::sync_with_stdio(false);
	ans[0]=-1;
	ans[1]=10;
	for(ll i=2;i<MAXN;i++)
	{
		SET(a,0);
		int f=0,c=1,val=i;
		while(1)
		{
			if(check(val))
			{
				break;
			}
			++c;
			val=c*i;
		}
		ans[i]=val;
		//cout<<ans[i]<<el;
	}
	int t,tt;
	cin>>tt;
	for(t=1;t<=tt;t++)
	{
		int n;
		cin>>n;
		if(ans[n]==-1)
			cout<<"Case #"<<t<<": INSOMNIA"<<el;
		else
			cout<<"Case #"<<t<<": "<<ans[n]<<el;
	}	
	return 0;
}