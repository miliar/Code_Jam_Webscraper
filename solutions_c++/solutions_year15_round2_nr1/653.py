#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<cmath>
#include<iomanip>
#include<cstdlib>
#include<sstream>
#include<climits>
#include<cassert>
#include<time.h>
using namespace std;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define pb push_back
#define ss second
#define ff first
#define vi vector<int>
#define vl vector<ll>
#define s(n) scanf("%d",&n)
#define ll long long
#define mp make_pair
#define PII pair <int ,int >
#define PLL pair<ll,ll>
#define inf 1000*1000*1000+5
#define v(a,size,value) vi a(size,value)
#define sz(a) a.size()
#define all(a) a.begin(),a.end()
#define tri pair < int , PII >
#define TRI(a,b,c) mp(a,mp(b,c))
#define xx ff
#define yy ss.ff
#define zz ss.ss
#define in(n) n = inp()
#define vii vector < PII >
#define vll vector< PLL >
#define viii vector < tri >
#define vs vector<string>
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end());
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define ok if(debug)
#define trace1(x) ok cerr << #x << ": " << x << endl;
#define trace2(x, y) ok cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)    ok      cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)  ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
								<< #d << ": " << d << endl;
#define trace5(a, b, c, d, e) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
									 << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
									<< #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
ll MOD = int(1e9) + 7;
#define gc getchar()//_unlocked()
inline int inp(){register int n=0,s=1,c=gc;if(c=='-')s=-1;while(c<48)c=gc;while(c>47)n=(n<<3)+(n<<1)+c-'0',c = gc;return n*s;}
#define pc(x) putchar//_unlocked(x);
inline void writeInt (int n)
{register  int N = n, rev, count = 0;rev = N; if (N == 0) { pc('0'); pc('\n'); return ;}
while ((rev % 10) == 0) { count++; rev /= 10;}rev = 0; while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}
while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}while (count--) pc('0'); }
const int N = 1000*100+5;
int debug = 1;
vi getdigits(ll n)
{
	vi ret;
	while(n != 0)
	{
		ret.pb(n%10);
		n /= 10;
	}
	reverse(all(ret));
	return ret;
}
ll get(ll i)
{
	ll num1 = pow(10,i/2) - 1;
	ll num2 = pow(10,(i+1)/2) - 1;
	return num1 + num2 + 1;
}
int check(vi a)
{
	int n = sz(a)/2;
	int i;
	if(a[0] != 1)
		return 0;
	for(i = 1; i < n;i++)
		if(a[i])
			return 0;
	return 1;
}
int check1(vi a)
{
	int i;
	int n = (sz(a)+1)/2;
	for(i = n; i < sz(a);i++)
		if(a[i] != 0)
			return 1;
	return 0;
}
ll calc1(vi a)
{
	int i,j;
	int n = sz(a)/2;
	vi temp;
	rep(i,n)
		temp.pb(a[i]);
	reverse(all(temp));
	ll ans1 = 0;
	rep(i,sz(temp))
		ans1 = ans1*10 + temp[i];
	ll ans2 = 0;
	f(i,n,sz(a))
	{
		ans2 = ans2*10 + a[i];
	}
	trace3(ans1,ans2,a.back());
	return ans1 + ans2 + 1 - 1;
}
ll solve(ll n)
{
	vi a = getdigits(n);
	int m = sz(a);
	ll ans = 0;
	int i;
	for(i = 1; i < m;i++)
	{
		if(i == 1)
			ans += 9;
		else if(i == 2)
			ans += 19;
		else
			ans += get(i);
	}
	ll num1 = n - pow(10,m-1);
	trace1(num1);
	if(!check1(a))
		return solve(n-1) + 1;
	if(check(a))
		return num1 + ans;
	return calc1(a) + ans;

}
int main()
{
	int i,j,n,t,t1;
	ios::sync_with_stdio(false);
	cin>>t;
	for(t1 = 1 ; t1 <= t; t1++)
	{
		ll n;
		cin>>n;
		trace1(n);
		ll ans;
		if(n <= 10)
			ans  = n;
		else
		 ans = solve(n) + 1;
		cout<<"Case #"<<t1<<": "<<ans<<endl;
	}
}
