// tsukasa_diary's programing contest code template
#include <bits/stdc++.h>
using namespace std;
#define TSUKASA_DIARY_S_TEMPLATE
// define
#define for_(i,a,b) for(int i=(a);i<(b);++i)
#define for_rev(i,a,b) for(int i=(a);i>=(b);--i)
#define allof(a) (a).begin(),(a).end()
#define minit(a,b) memset(a,b,sizeof(a))
#define size_of(a) int((a).size())
#define cauto const auto
// typedef
typedef long long lint;
typedef double Double;
typedef pair< int, int > pii;
template< typename T > using Vec = vector< T >;
template< typename T > using Matrix = Vec< Vec< T > >;
template< typename T > using USet = unordered_set< T >;
template< typename T, class C > using MyUSet = unordered_set< T, C >;
template< typename T, typename F > using UMap = unordered_map< T, F >;
template< typename T, typename F, class C > using MyUMap = unordered_map< T, F, C >;
// hash
class PiiHash { public: size_t operator () (const pii& p) const { return (p.first << 16) | p.second; } };
// popcount
inline int POPCNT(int x) { return __builtin_popcount(x); }
inline int POPCNT(lint x) { return __builtin_popcount(x); }
// inf
const int iINF = 1L << 30;
const lint lINF = 1LL << 60;
// eps
const Double EPS = 1e-9;
const Double PI = acos(-1);
// inrange
template< typename T >
inline bool in_range(T v, T mi, T mx) { return mi <= v && v < mx; }
template< typename T >
inline bool in_range(T x, T y, T W, T H) { return in_range(x,0,W) && in_range(y,0,H); }
// neighbor clockwise
const int DX[4] = {0,1,0,-1}, DY[4] = {-1,0,1,0};
const int DX_[8] = {0,1,1,1,0,-1,-1,-1}, DY_[8] = {-1,-1,0,1,1,1,0,-1};
// variable update
template< typename T > inline void modAdd(T& a, T b, T mod) { a = (a + b) % mod; }
template< typename T > inline void minUpdate(T& a, T b) { a = min(a, b); }
template< typename T > inline void maxUpdate(T& a, T b) { a = max(a, b); }
// converter
template< typename F, typename T >
inline void convert(F& from, T& to) {
	stringstream ss;
	ss << from; ss >> to;
}

int N, K;
double P[222];
double dp[201][202][102];

void solve() {
	cin >> N >> K;
	for_(i,0,N) cin >> P[i];
	
	double sp = (double)K / (double)N;
	int mK = K / 2;
	
	minit(dp, 0);
	dp[0][0][0] = 1.0;
	
	for_(i,0,N) {
		double yp = P[i];
		double np = 1.0 - yp;
		
		for_(ii,0,K+1) {
		for_(y,0,mK+1) {
			dp[i + 1][ii][y] += dp[i][ii][y] * (1.0 - sp);
			dp[i + 1][ii + 1][y + 1] += dp[i][ii][y] * sp * yp;
			dp[i + 1][ii + 1][y] += dp[i][ii][y] * sp * np;
		}
		}
	}
	
	cout << setprecision(9) << setiosflags(ios::fixed) << dp[N][K][mK] << endl;
}

double calc(Vec< int >& use) {
	double res = 0.0;
	
	int S = (1 << (K / 2)) - 1;
	while (S < (1 << K)) {
		double add = 1.0;
		
		for_(i,0,K) {
			int ii = use[i];
			if ((S >> i) & 1) add *= P[ii];
			else add *= (1.0 - P[ii]);
		}
		
		res += add;
		
		int x = S & -S, y = S + x;
		S = ((S & ~y) / x >> 1) | y;
	}
	
	return res;
}

void small() {
	cin >> N >> K;
	for_(i,0,N) cin >> P[i];
	
	double ans = 0.0;
	
	int S = (1 << K) - 1;
	while (S < (1 << N)) {
		Vec< int > use;
		for_(i,0,N) if ((S >> i) & 1) use.push_back(i);
		
		maxUpdate(ans, calc(use));
		
		int x = S & -S, y = S + x;
		S = ((S & ~y) / x >> 1) | y;
	}
	
	cout << setprecision(9) << setiosflags(ios::fixed) << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for_(i,0,T) {
		cout << "Case #" << i + 1 << ": ";
		small();
		//solve();
	}
}
