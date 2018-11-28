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
#define mx 1000000
bool base[mx];
int primes[mx];
int sz;

void sieve() {
	int x = sqrt(mx);

	for(int i = 3; i <= x; i += 2) if(base[i] == 0) for(int j = i*i, k = i<<1; j < mx; j += k) base[j] = 1;

	sz = 0;
	for(int i = 3; i < mx; i += 2) if(base[i] == 0) primes[sz++] = i;
}

int checkPrime(ll n) {
	int x = sqrt(n);
	for(int i = 0; primes[i] <= x; ++i) if(n%primes[i] == 0) return primes[i];
	return 0;
}

void show(ll n) {
	rep(i, 32) printf("%d", checkBit(n, i));
}

vector <pair <ll, vi> > ans;

int main () {
	sieve();

	for(ll mask = 1; mask < (1LL<<31); mask += 2) {
		ll nmask = mask|(1LL<<31);

		vi divs;

		//checking perliminarity
		int flag = 1;

		for(int b = 2; b <= 10; ++b) {

			int tmp = 0;
			for(int j = 1; j < sz; ++j) {
				ll n = 0;
				rep(i, 32) {
					n = n*b;
					n += checkBit(nmask, i);
					n %= primes[j];
				}

				if(n == 0) {
					divs.PB(primes[j]);
					tmp = 1;
					break;
				}
			}
			if(tmp == 0) {
				flag = 0;
				break;
			}
		}

		if(flag == 0) continue;

		ans.PB({nmask, divs});

		if(ans.size() == 500) break;
	}

	int t, x, y;

	si(t);

	while(t--) sii(x, y);

	printf("Case #%d:\n", 1);
	rep(i, 500) {
		show(ans[i].F);
		rep(j, 9) printf(" %d", ans[i].S[j]);
		nl;
	}
	
	return 0;
}
