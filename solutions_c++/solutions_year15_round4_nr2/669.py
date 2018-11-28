#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii > vii;
typedef vector<pair<int, pair<int, int> > > viii;
typedef pair<ll,ll> pll;
typedef vector<string> vs;
typedef vector<vii> vvii;

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define MEM(a,b) memset(a,(b),sizeof(a))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) cin>>((a)[i])  
#define md 1000000007
#define MAXN 200005


// #define pr16

#ifdef pr16
  #define pr(x)                 cerr << #x << ": " << x << endl;
  #define pr2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
  #define pr3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
  #define pr4(a, b, c, d)       cerr <<fixed<<setprecision(10)<< #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
  #define pr5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
  #define pr6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
  #define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cerr<<a[i][j]<<" "; cerr<<endl; } cerr<<endl;
  #define prc(a) tr(a, it) cerr<<*(it)<<" "; cerr<<endl
  #define pra(a,n) for(int i=0; i<(n); i++) cerr<<((a)[i])<<" "; cerr<<"\n"
  #define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cerr<<a[i][j]<<" "; cerr<<endl; } cerr<<endl; 
  #define prddd(a,x,y,z) for(int i=0;i<x;i++) {cerr<<"layer "<<i<<":\n";prdd(a[i],y,z)}

#else
  #define pr(x)
  #define pr2(x, y)
  #define pr3(x, y, z)
  #define pr4(a, b, c, d)
  #define pr5(a, b, c, d, e)
  #define pr6(a, b, c, d, e, f)
  #define tr(c,it)
  #define prc(a)
  #define pra(a,n)
  #define prdd(a, r, c)
  #define prddd(a,x,y,z)
#endif

int n;
double v,tp;
double r[100],t[100];
vector< pair<double,double > > vc;

int check(double x)
{
	double tmp = 0,vol = 0;

	rep(i,n)
	{
		if(v - vol - vc[i].Y*x > -1e-11)
		{
			tmp = (tmp*vol+x*vc[i].X*vc[i].Y)/(vol+vc[i].Y*x);
			vol += (vc[i].Y*x);
		}
		else
		{
			tmp = (tmp*vol+vc[i].X*(v-vol))/(v);
			vol = v;
		}
	}
	pr4(tmp,tp,vol,v);
	if(tmp > tp+1e-11 or vol < v-1e-11)
		return 0;
	pr(n);
	tmp = 0,vol = 0;
	for(int i = n-1;i>=0;i--)
	{
		if(v - vol - vc[i].Y*x > 1e-11)
		{
			tmp = (tmp*vol+x*vc[i].X*vc[i].Y)/(vol+vc[i].Y*x);
			vol += (vc[i].Y*x);
			
		}

		else
		{
			tmp = (tmp*vol+vc[i].X*(v-vol))/v;
			vol = v;
		}
	}
	if(tmp < tp-1e-11 or vol < v-1e-11)
		return 0;
	return 1;
}

void fn()
{	
	vc.clear();
	cin>>n>>v>>tp;
	// pr3(n,v,tp);
	rep(i,n)
		cin>>r[i]>>t[i];
	// pra(r,n);
	// pra(t,n);
	
	rep(i,n)
		vc.pb(mp(t[i],r[i]));
	sort(all(vc));
	if(vc[0].X > tp+1e-11 or vc[n-1].X < tp-1e-11)
	{
		cout<<"IMPOSSIBLE\n";
		return;
	}
	double l = 1e-11,r = 1e30;
	// pr(check(10000000));
	while(r-l>=1e-8)
	{
		double m = (l+r)/2;
		if(check(m) == 0)
			l = m;
		else
			r = m;
		// pr2(m,check(m));
	}
	cout<<fixed<<setprecision(10)<<l<<"\n";
}

int main()
{   
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    rep(i,t)
    {	
    
    	cout<<"Case #"<<i+1<<": ";
    	fn();
    }

    return 0;
}
