#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

const int MAX = 30;

int n;
char g[MAX][MAX];
char tg[MAX][MAX];
int wu, mu;

unsigned int numbits(unsigned int i)
{
	const unsigned int MASK1 = 0x55555555;
	const unsigned int MASK2 = 0x33333333;
	const unsigned int MASK4 = 0x0f0f0f0f;
	const unsigned int MASK8 = 0x00ff00ff;
	const unsigned int MASK16 = 0x0000ffff;
	i = (i&MASK1) + (i >> 1 & MASK1);
	i = (i&MASK2) + (i >> 2 & MASK2);
	i = (i&MASK4) + (i >> 4 & MASK4);
	i = (i&MASK8) + (i >> 8 & MASK8);
	i = (i&MASK16) + (i >> 16 & MASK16);
	return i;
}

void clear() {
}

void read() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%s", g[i]);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			g[i][j] -= '0';
}

pii findWorkers(int wi);

pii findMachines(int wi) {
	wu |= 1 << wi;
	int wm = 1 << wi, mm = 0;
	for (int mi = 0; mi < n; mi++)
		if (tg[wi][mi] && !(mu >> mi & 1)) {
			pii p = findWorkers(mi);
			wm |= p.first, mm |= p.second;
		}
	return pii(wm, mm);
}

pii findWorkers(int mi) {
	mu |= 1 << mi;
	int wm = 0, mm = 1 << mi;
	for (int wi = 0; wi < n; wi++)
		if (tg[wi][mi] && !(wu >> wi & 1)) {
			pii p = findMachines(wi);
			wm |= p.first, mm |= p.second;
		}
	return pii(wm, mm);
}

bool check() {
	wu = 0, mu = 0;
	for (int wi = 0; wi < n; wi++) {
		if (wu >> wi & 1) continue;
		pii p = findMachines(wi);
		if (p.first == 0 || p.second == 0) return false;
		if (numbits(p.first) != numbits(p.second)) return false;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if ((p.first >> i & 1) && (p.second >> j & 1))
					if (tg[i][j] == 0) return false;
	}
	return true;
}

int solve() {
	int m = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			m |= (1 << i * n + j) * g[i][j];

	int res = INF;
	for (int tm = 0; tm < 1 << n * n; tm++) {
		if ((m & tm) != m) continue;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				tg[i][j] = tm >> (i * n + j) & 1;
		if (!check()) continue;
		int tres = numbits(tm) - numbits(m);
		res = min(res, tres);
	}
	return res;
}

int main() {
#ifdef _LOCAL_VAN
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int it = 1; it <= t; it++) {
		clear();
		read();
		int res = solve();
		printf("Case #%d: %d\n", it, res);
	}
	return 0;
}