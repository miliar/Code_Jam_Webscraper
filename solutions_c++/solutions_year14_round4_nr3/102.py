// @betaveros :: vim:set fdm=marker syntax=cppc:
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

struct Rect {
	int xlo, xhi, ylo, yhi;
	Rect() {}
	Rect(int xlo, int xhi, int ylo, int yhi):
		xlo(xlo), xhi(xhi), ylo(ylo), yhi(yhi) {}
	void scan() { scan_dddd(xlo, ylo, xhi, yhi); }
	ll operator-(const Rect & o) {
		return max(0,
			max(max(ylo - o.yhi, o.ylo - yhi),
			max(xlo - o.xhi, o.xlo - xhi)) - 1);
	}
} rects[1008];

int w, h, b;
void readInput() {
	scan_ddd(w, h, b);
	fori (i, 0, b) {
		rects[i].scan();
	}
}
bool vis[1008];
ll dist[1008];
ll OO = 2000000000000000000;
ll kr() {
	int six = b, eix = b + 1;
	rects[six] = Rect(-1,-1,0,100000000);
	rects[eix] = Rect( w, w,0,100000000);
	dist[six] = 0;
	fill(vis, vis + 1008, 0);
	vis[six] = true;
	fori (i, 0, eix+1) {
		dist[i] = rects[six] - rects[i];
		debugf("init dist = %lld\n", dist[i]);
	}
	while (!vis[eix]) {
		int nxt = -1;
		int nd = OO;
		fori (i, 0, eix+1) {
			if (!vis[i] && dist[i] < nd) {
				nxt = i;
				nd = dist[i];
			}
		}
		debugf("vis %d\n", nxt);
		vis[nxt] = true;
		fori (i, 0, eix+1) {
			minify(dist[i], dist[nxt] + (rects[nxt] - rects[i]));
		}
	}
	return dist[eix];
}


void tc(int tci) {
	readInput();
	printf("Case #%d: %lld", tci, kr());
	printf("\n");
}

int main() {
	int tcn;
	scanf("%d", &tcn);
	fori (i, 0, tcn) tc(i+1);
}
