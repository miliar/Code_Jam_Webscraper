/*
ID: tahsynx1
LANG: C++
TASK: 
*/

#include <bits/stdc++.h>
using namespace std;

//typedefs
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef vector <int> vi;
typedef vector <ll> vl;
typedef pair <ll, ll> pll;
const double PI = acos(-1);

//defines
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define mem(a, b) memset(a, b, sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a)*(a))
#define inf 100000000
#define mod 1000000007
#define mod1 1000000007
#define mod2 1000000009
#define b1 43
#define b2 41
#define EPS 1e-9
//define harmonic(n) 0.57721566490153286l+log(n)
#define nl puts("")
#define odd(n) (n&1)
#define even(n) (!(n&1))

//loop
#define rep(i, n) for(int i = 0; i < n; ++i)
#define REP(i, n) for(int i = 1; i <= n; ++i)

//input
#define si(a) scanf("%d", &a)
#define sii(a, b) scanf("%d%d", &a, &b)
#define siii(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define sl(a) scanf("%lld", &a)
#define sll(a, b) scanf("%lld%lld", &a, &b)
#define slll(a, b, c) scanf("%lld%lld%lld", &a, &b, &c)
#define sd(a) scanf("%lf", &a)
#define sc(a) scanf("%c", &a)
#define sst(a) scanf("%s", a)

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

//debug
#ifdef tahsin
template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) { return os << "(" << p.first << ", " << p.second << ")"; }

template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) { os << "{";
	for(auto it = v.begin(); it != v.end(); ++it) { if( it != v.begin() ) os << ", "; os << *it; }
    return os << "}"; }

template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) { os << "[";
	for(auto it = v.begin(); it != v.end(); ++it) { if( it != v.begin() ) os << ", "; os << *it; }
    return os << "]"; }

template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) { os << "[";
	for(auto it = v.begin(); it != v.end(); ++it) { if( it != v.begin() ) os << ", "; os << it -> first << " = " << it -> second ; }
    return os << "]"; }

#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)

clock_t tStart = clock();
#define timeStamp dbg("Execution Time: ", (double)(clock() - tStart)/CLOCKS_PER_SEC)

void faltu () { cerr << endl; }

template <typename T>
void faltu( T a[], int n ) { for(int i = 0; i < n; ++i) cerr << a[i] << ' '; cerr << endl; }

template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) { cerr << arg << ' '; faltu(rest...); }

#else
#define dbg(args...)
#endif

ll bigmod(ll a, ll b) {
	ll ret = 1;
	while(b) { if(b&1) ret = (ret*a)%mod; b >>= 1; a = (a*a)%mod; }
	return ret;
}

ll inverse(ll n) { return bigmod(n, mod-2); }

//Direction Array 
//int fx[]={1, -1, 0, 0}; int fy[]={0, 0, 1, -1};
//int fx[]={0, 0, 1, -1, -1, 1, -1, 1}; int fy[]={-1, 1, 0, 0, 1, 1, -1, -1};

//bit manipulation
bool checkBit(int n, int i) { return (n&(1<<i)); }
int setBit(int n, int i) { return (n|(1<<i)); }
int resetBit(int n, int i) { return (n&(~(1<<i))); }
//end of template

//#define MX 

int n, tot, paisi;
vector <vi> a;
vi res;

void bt(int prev) {
	if((int) res.size() == n) {
		for(int i = 1; i < n; ++i) for(int j = 0; j < n; ++j) if(a[res[i]][j] <= a[res[i-1]][j]) return;

		vi cnt(tot);
		rep(i, n) cnt[res[i]] = 1;

		vector <vi> ans;
		rep(j, n) {
			vi v;
			rep(i, n) v.PB(a[res[i]][j]);


			int flag = 0;
			rep(i, tot) {
				if(cnt[i]) continue;
				if(v == a[i]) {
					flag = 1;
					break;
				}
			}
			if(flag == 0) ans.PB(v);

		}

		if((int) ans.size() == 1) {
			paisi = 1;

			rep(i, n) printf(" %d", ans[0][i]);
			nl;
		}

		return;
	}

	if(paisi) return;
	for(int i = prev+1; i < tot; ++i) {
		if(paisi) return;
		int flag = 1;
		for(int j = 0; j < n; ++j) if(a[i][j] <= a[prev][j]) {
			flag = 0;
			break;
		}
		if(paisi) return;
		if(flag) {
			res.PB(i);
			bt(i);
			res.pop_back();
		}
	}

}

int main () {
#ifdef tahsin
	freopen("out", "w", stdout);
#endif
	int t, x;

	si(t);
	dbg(t);

	REP(cs, t) {
		si(n);

		tot = n*2-1;

		rep(i, tot) {
			vi v;
			rep(j, n) {
				si(x);
				v.PB(x);
			}
			a.PB(v);
		}

		sort(a.begin(), a.end());

		paisi = 0;

		printf("Case #%d:", cs);

		rep(i, n) {
			if(paisi) break;
			res.PB(i);
			bt(i);
			res.pop_back();
		}

		res.clear();
		a.clear();
	}

//	timeStamp;
	return 0;
}

