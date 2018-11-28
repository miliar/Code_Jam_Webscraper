// tsukasa_diary's programing contest code template
#include <bits/stdc++.h>
using namespace std;
// define
#define for_(i,a,b) for(int i=(a);i<(b);++i)
#define for_rev(i,a,b) for(int i=(a);i>=(b);--i)
#define allof(a) (a).begin(),(a).end()
#define minit(a,b) memset(a,b,sizeof(a))
#define size_of(a) int((a).size())
// typedef
typedef long long lint;
typedef double Double;
typedef pair< int, int > pii;
template< typename T >
using Matrix = vector< vector< T > >;
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

int count(int val, int y) {
	int res = 0;
	
	while (val > y) {
		val -= y;
		++res;
	}
	
	return res;
	
	/*
	priority_queue< int > que;
	que.push(val);
	
	int res = 0;
	
	while (que.top() > y) {
		int t = que.top(); que.pop();
		que.push(t / 2);
		que.push(t / 2 + (t % 2));
		++res;
	}
	
	return res;
	*/
}

int solve(int D, vector< int >& P) {
	int ans = iINF;
	
	for_(y,1,1010) {
		int cnt = 0;
		for_(i,0,D) cnt += count(P[i], y);
		ans = min(ans, cnt + y);
	}
	
	return ans;
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		int D;
		cin >> D;
		
		vector< int > P(D, 0);
		for_(i,0,D) cin >> P[i];
		
		cout << "Case #" << i + 1 << ": " << solve(D, P) << endl;
	}
}