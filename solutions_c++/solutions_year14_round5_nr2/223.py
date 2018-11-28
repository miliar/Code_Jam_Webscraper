// @betaveros :: vim:set fdm=marker:
#define NDEBUG
// #includes, using namespace std {{{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
// #include <cinttypes> // C++11?
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <new>
#include <algorithm>
#include <iostream>
using namespace std;
// }}}
// #defines, typedefs, constants {{{
#define fori(i,s,e) for(int i = s; i < ((int)e); i++)
#define forui(i,s,e) for(unsigned int i = s; i < ((unsigned int)e); i++)
#define foruin(i,c) for(unsigned int i = 0; i < ((unsigned int)(c).size()); i++)
#define _conc(x,y) x ## y
#define _conc2(x,y) _conc(x,y)
#define repeat(n) fori(_conc2(_,__LINE__),0,n)
#define allof(s) (s).begin(), (s).end()
#define scan_d(x) scanf("%d",&(x))
#define scan_dd(x,y) scanf("%d%d",&(x),&(y))
#define scan_ddd(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define scan_dddd(x,y,z,w) scanf("%d%d%d%d",&(x),&(y),&(z),&(w))
#define pushb push_back
#define popb push_back

#ifdef NDEBUG
#define debug(code)
#define debugf(...) ((void)0)
#else
#define debug(code) code
#define debugf(...) fprintf(stderr, __VA_ARGS__)
#endif
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> Vint;
typedef vector<int>::iterator Vit;

// const int OO  = 1000 << 10;
// const int OO2 = 2000 << 10;
// const int       M7  = 1000000007;
// const int       M9  = 1000000009;
// const long long M7L = 1000000007L;
// }}}
// dump, min/maxify {{{
template <class T> void dumpBetween(const T & a, const T & b) {
	for (T it = a; it != b; it++) cout << *it << " ";
	cout << endl;
}
template <class T> void dumpAll(const T & a) { dumpBetween(allof(a)); }
template <class T> void minify(T & a, const T & b) { if (a > b) a = b; }
template <class T> void maxify(T & a, const T & b) { if (a < b) a = b; }
// }}}

const int JN = 2111;
ll dp[108][JN];
int n, p, q, h[108], g[108];
void readInput() {
	scan_ddd(p, q, n);
	fori (i, 0, n) {
		scan_dd(h[i], g[i]);
	}
}

ll dpget(int i, int j) {
	if (i >= n || j < 0) return 0;
	j = min(j, JN - 1);
	return dp[i][j];
}

void tc(int tci) {
	readInput();

	ll tg = 0;
	fori (i, 0, n) tg += g[i];
	fori (i, 0, n) dp[i][JN - 1] = tg;
	for (int i = n - 1; i >= 0; i--) {
		int waste = (h[i] - 1) / q;
		int rem = h[i] - waste * q;
		assert(rem > 0);
		int remreq = (rem + p - 1) / p;
		for (int j = JN - 2; j >= 0; j--) {
			dp[i][j] = dpget(i+1, j + waste + 1);
			if (j + waste >= remreq)
				maxify(dp[i][j], g[i] + dpget(i+1, j + waste - remreq));
			debugf("%d %d = %lld\n", i, j, dp[i][j]);
		}
	}

	printf("Case #%d: ", tci);
	printf("%lld", dp[0][1]);
	printf("\n");
}

int main() {
	int tcn;
	scanf("%d", &tcn);
	fori (i, 0, tcn) tc(i+1);
}

