#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

int R, C;
int a[120][120];
int maxr[120], maxc[120];

bool solve() {
	memset(maxr, 0, sizeof maxr);
	memset(maxc, 0, sizeof maxc);
	GI2(R, C);
	REP(r, R) REP(c, C) {
		GI(a[r][c]);
		maxr[r] = max(maxr[r], a[r][c]);
		maxc[c] = max(maxc[c], a[r][c]);
	}

	REP(r, R) REP(c, C) if (a[r][c] < min(maxr[r], maxc[c]))
		return false;
	return true;
}

int main() {
//freopen("input.txt", "rt", stdin);

freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		int res = solve();
		printf("Case #%d: %s\n", tc, res ? "YES" : "NO");
	}

}
