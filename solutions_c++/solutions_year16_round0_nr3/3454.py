#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*int divisor(ll n) 
{
	for (int d = 2; d*d <= n; ++d) {
		if (n % d == 0) return d;
	}
	return 0;
}*/

ll divisor(ll n) 
{
	if ((n&1) == 0) return 2;
	if(n%3 == 0) return 3;
	for (ll x = 5, xsq = 25, xsqd = 96; xsq > 0 && xsq <= n; x+=6, xsq+=xsqd, xsqd+=72) {
		if (n%x == 0) return x;
		if (n%(x+2) == 0) return x+2;
	}
	return 0;
}

void Solve(int tc)
{
	int N, J;
	scanf("%d%d", &N, &J);
	printf("Case #%d:\n", tc);
	REP(i, two(N-2)) {
		int X = two(N-1) | (i<<1) | 1;
		vector<ll> v;
		FOR(base, 2, 10) {
			ll Y = 0;
			REP(j, N) Y = Y * base + ((X>>(N-1-j))&1);
			ll d = divisor(Y);
			if (d) v.push_back(d);
			else break;
		}
		if (v.size() == 9) {
			REP(j, N) printf("%d", (X>>(N-1-j))&1);
			REP(j, v.size()) printf(" %lld", v[j]);
			printf("\n");
			if (--J == 0) break;
		}
	}
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) {
		cerr << "Test case: " << tc << endl;
		Solve(tc);
	}

	return 0;
}