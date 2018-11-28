#include<bits/stdc++.h>
 
#define pb push_back
#define len(n) n.length()
#define mp make_pair
#define forp(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,n)    for(ll i=0;i<n;i++)
#define ren(i,n)    for(ll i=n-1;i>=0;i--)
#define forn(i,a,b) for(int i=a;i>=b;i--)
//#define fre(A, B)     freopen(A,"r",stdin),freopen(B,"w",stdout)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define vll vector<long long int>
#define all(n) n.begin(),n.end()
#define alll(n,i,j) n.begin()+i,n.begin()+j
#define present(s,x) (s.find(x) != s.end())
#define cpresent(s,x) (find(all(s),x) != s.end())
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define mem(n,m) memset(n,m,sizeof(n))
#define bitc(n) __builtin_popcount(n)
#define mod 1000000007
#define mod2 1000000009
#define ma(m,n) m = max(m,n)
#define mi(m,n) m = min(m,n)
#define EPSILON 1e-6
#define PI 3.14159265358979323846
 
#define TRACE
 
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
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef vector<vector<ll> > mat;
//#define N 100005
#define INF mod

bool cnt[11];

int main () {
 freopen("A-large.in","r",stdin),freopen("op.out","w",stdout);
 int t;
 cin >> t;
 forp (TT,1,t) {
 	mem(cnt, false);
 	int N;
 	cin >> N;
 	if (N == 0) {
 	  cout << "Case #" << TT << ": INSOMNIA" << "\n";
 	  continue;
	}
 	ll n = N;
 	while (true) {
 	  ll num = n;
 	  while (num) {
 	   cnt[num % 10] = true;
	   num /= 10;	
	  }
	  int sleep = 0;
	  rep (i,10) {
	  	sleep += cnt[i] == true;
	  }
	  if (sleep == 10) {
	  	break;
	  }
	  n += N;
	}
	cout << "Case #" << TT << ": " << n << "\n";
 }
 return 0;
}
