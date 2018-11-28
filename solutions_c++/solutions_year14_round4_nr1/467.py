#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <utility>
#include <sstream>
#include <numeric>

#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <cmath>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define dbgv(v) do{cerr<<#v<<':';for(auto x:v) cerr << x << ','; cerr << '\n';}while(0)
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define ford1(i, n) for(int i = (int)(n); i>=1; --i)
#define fored(i, a, b) for(int i = (int)(b); i >= (int)(a); --i)
#define sz(v) ((int)((v).size()))
#define all(v) (v).begin(), (v).end()
#define clr(v) memset(v, 0, sizeof(v))
#define clr1(v) memset(v, 0xFF, sizeof(v))
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define op operator

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef long long i64;
typedef unsigned long long u64;	
typedef long double ld;

const int MOD = 1000000007;

int popcnt(int x) { return __builtin_popcount(x);}
int popcnt(u64 x) { return __builtin_popcountll(x);}
int ctz(int x) { return __builtin_ctz(x);}
int ctz(u64 x) { return __builtin_ctzll(x);}
int clz(int x) { return __builtin_clz(x);}
int clz(u64 x) { return __builtin_clzll(x);}
int ffs(int x) { return __builtin_ffs(x);}
int ffs(u64 x) { return __builtin_ffsll(x);}
int parity(int x) { return __builtin_parity(x);}
int parity(u64 x) { return __builtin_parityll(x);}
double powi(double x, int i) { return __builtin_powi(x,i); }
float powi(float x, int i) { return __builtin_powif(x,i); }
long double powi(long double x, int i) { return __builtin_powil(x,i); }
int gcd(int a, int b) { return __gcd(a,b); }
i64 gcd(i64 a, i64 b) { return __gcd(a,b); }
int lcm(int a, int b) { return a/__gcd(a,b)*b; }
i64 lcm(i64 a, i64 b) { return a/__gcd(a,b)*b; }

int add(int a, int b) { a += b; if(a>=MOD) a-= MOD; return a; }
int sub(int a, int b) { a -= b; if(a<0) a+= MOD; return a; }
int mul(int a, int b) { return (a*1ll*b) % MOD; }
inline int pow(int a, i64 n) { int r(1); while(n) { if(n&1) r=mul(r,a); n/=2; if(n)a=mul(a,a);} return r; }

inline bool randb() {
    static int x, pos = -1;
    if(pos==-1) { pos = 30; x = rand(); }
    return (x>>(pos--))&1;
}

template<class T> bool uax(T&a, const T& b) {
	if( a < b ) { a = b; return true; }
	return false;
}

template<class T> bool uin(T&a, const T& b) {
	if( a > b ) { a = b; return true; }
	return false;
}

const ld pi = acosl(-1.0);
const ld eps = 1e-9;

void solve() {
    int n, S;
    scanf("%d%d", &n, &S);
    multiset<int> a;
    forn(i, n) {
        int x; scanf("%d", &x);
        a.insert(x);
    }
    int r = 0;
    while( !a.empty() ) {
        ++r;
        int l = S - *a.rbegin();
        auto eit = a.end(); --eit;
        a.erase(eit);
        auto it = a.upper_bound(l);
        if( it != a.begin() ) {
            --it;
            a.erase(it);
        }
    }
    printf("%d\n", r);
    return;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
	cout << fixed;
	cout.precision(15);
	cerr << fixed;
	cerr.precision(15);
    int T; scanf("%d", &T);
    forn(t, T) {
        printf("Case #%d: ", t+1);
        solve();
    }
    return 0;
}
