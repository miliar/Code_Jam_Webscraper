#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef vector<int> vint;
typedef pair<int,int> pint;
#define mp make_pair

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T &t, const T &f) { if (t > f) t = f; }
template<typename T> void chmax(T &t, const T &f) { if (t < f) t = f; }
int in() { int x; scanf("%d", &x); return x; }

namespace MF {
	#define MAXN 1000010
	#define MAXM 2000010
	#define wint int
	const wint wEPS = 0;
	const wint wINF = 1001001001;
	int n, m, ptr[MAXN], next[MAXM], zu[MAXM];
	wint capa[MAXM], tof;
	int lev[MAXN], see[MAXN], que[MAXN], *qb, *qe;
	void init(int _n) {
		n = _n; m = 0; memset(ptr, ~0, n * 4);
	}
	void ae(int u, int v, wint w0, wint w1 = 0) {
		next[m] = ptr[u]; ptr[u] = m; zu[m] = v; capa[m] = w0; ++m;
		next[m] = ptr[v]; ptr[v] = m; zu[m] = u; capa[m] = w1; ++m;
	}
	wint augment(int src, int ink, wint flo) {
		if (src == ink) return flo;
		wint f;
		for (int &i = see[src]; ~i; i = next[i]) if (capa[i] > wEPS && lev[src] < lev[zu[i]]) {
			if ((f = augment(zu[i], ink, min(flo, capa[i]))) > wEPS) {
				capa[i] -= f; capa[i ^ 1] += f; return f;
			}
		}
		return 0;
	}
	bool solve(int src, int ink, wint flo = wINF) {
		wint f;
		int i, u, v;
		for (tof = 0; tof + wEPS < flo; ) {
			qb = qe = que;
			memset(lev, ~0, n * 4);
			for (lev[*qe++ = src] = 0, see[src] = ptr[src]; qb != qe; ) {
				for (i = ptr[u = *qb++]; ~i; i = next[i]) if (capa[i] > wEPS && !~lev[v = zu[i]]) {
					lev[*qe++ = v] = lev[u] + 1; see[v] = ptr[v];
					if (v == ink) goto au;
				}
			}
			return 0;
		au:	for (; (f = augment(src, ink, flo - tof)) > wEPS; tof += f);
		}
		return 1;
	}
}

const int DX[] = { +1,  0, -1,  0, };
const int DY[] = {  0, +1,  0, -1, };

int W, H;
int B;
int X0[1010], Y0[1010], X1[1010], Y1[1010];
bool is[510][510];

inline int IN (int x, int y) { return 2 + (x * H + y) * 2    ; }
inline int OUT(int x, int y) { return 2 + (x * H + y) * 2 + 1; }

int main() {
	
	
	for (int TC = in(), tc = 1; tc <= TC; ++tc) {
		W = in();
		H = in();
		B = in();
		for (int b = 0; b < B; ++b) {
			X0[b] = in();
			Y0[b] = in();
			X1[b] = in() + 1;
			Y1[b] = in() + 1;
		}
		memset(is, 0, sizeof(is));
		for (int b = 0; b < B; ++b) {
			for (int x = X0[b]; x < X1[b]; ++x) for (int y = Y0[b]; y < Y1[b]; ++y) {
				is[x][y] = true;
			}
		}
// for(int y=H;y--;){for(int x=0;x<W;++x)cout<<is[x][y];cout<<endl;}
		MF::init(2 + W * H * 2);
		for (int x = 0; x < W; ++x) for (int y = 0; y < H; ++y) if (!is[x][y]) {
			MF::ae(IN(x, y), OUT(x, y), 1);
		}
		for (int x = 0; x < W; ++x) {
			MF::ae(0, IN(x, 0), 1);
			MF::ae(OUT(x, H - 1), 1, 1);
		}
		for (int x = 0; x < W; ++x) for (int y = 0; y < H; ++y) if (!is[x][y]) {
			for (int h = 0; h < 4; ++h) {
				const int xx = x + DX[h];
				const int yy = y + DY[h];
				if (0 <= xx && xx < W && 0 <= yy && yy < H) if (!is[xx][yy]) {
					MF::ae(OUT(x, y), IN(xx, yy), 1);
				}
			}
		}
		MF::solve(0, 1);
		printf("Case #%d: %d\n", tc, MF::tof);
	}
	
	return 0;
}

