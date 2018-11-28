// @betaveros v1.1 :: vim:set fdm=marker syntax=cppc:
// #define NDEBUG
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
#define fori0(i,e) for(int i = 0; i < ((int)e); i++)
#define fori1(i,e) for(int i = 1; i <= ((int)e); i++)
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
#ifdef CDEBUG
#define debugf(...) fputs("\033[35m", stderr);fprintf(stderr, __VA_ARGS__);fputs("\033[0m", stderr)
#else
#define debugf(...) fprintf(stderr, __VA_ARGS__)
#endif
#endif
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector<int> Vint;
typedef vector<int>::iterator Vit;

// const int OO  = 1000 << 20;
// const int OO2 = 2000 << 20;
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

struct Pt {
	int x, y, z;
	double dist(const Pt & o) const {
		int xd = x - o.x;
		int yd = y - o.y;
		int zd = z - o.z;
		return sqrt(xd*xd + yd*yd + zd*zd);
	}
};
int n;

const int N = 1008;
Pt pts[N];
double dist[N];
bool vis[N];
int parent[N];
int jumpTime;

void readInput() {
	scan_dd(n, jumpTime);
	fori (i, 0, n) {
		scan_ddd(pts[i].x, pts[i].y, pts[i].z);
		int vx, vy, vz;
		scan_ddd(vx, vy, vz);
	}
}
double solve() {
	fori (i, 0, n) {
		dist[i] = pts[0].dist(pts[i]);
		vis[i] = false;
		parent[i] = 0;
	}
	dist[0] = 0;
	vis[0] = true;
	parent[0] = -1;
	while (true) {
		double mindist = 1e9;
		int minv = -1337;
		fori (i, 0, n) {
			if (!vis[i] && dist[i] < mindist) {
				mindist = dist[i];
				minv = i;
			}
		}
		// visit
		vis[minv] = true;
		fori (j, 0, n) {
			if (!vis[j] && pts[minv].dist(pts[j]) < dist[j]) {
				dist[j] = pts[minv].dist(pts[j]);
				parent[j] = minv;
			}
		}
		
		if (minv == 1) break;
	}
	double ret = 0;
	int cur = 1;
	while (cur != 0) {
		maxify(ret, dist[cur]);
		cur = parent[cur];
	}
	return ret;
}

void tc(int tci) {
	readInput();
	printf("Case #%d: %.15f", tci, solve());
	printf("\n");
}

int main() {
	int tcn;
	scanf("%d", &tcn);
	fori (i, 0, tcn) tc(i+1);
}
