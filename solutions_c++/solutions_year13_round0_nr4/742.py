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


int f[1<<20];
int n;
int cnt[222];
int key[20];
VI has[20];

bool go(int mask) {
	if (f[mask] != -1)
		return f[mask] >= 0;

	f[mask] = -2;
	FI if (!(mask & (1 << i))) if (cnt[ key[i] ]) {
		--cnt[key[i]];
		FJR(has[i].size()) ++cnt[ has[i][j] ];
		bool ok = go(mask | (1 << i));
		FJR(has[i].size()) --cnt[ has[i][j] ];
		++cnt[key[i]];

		if(ok) {
			f[mask] = i;
			return true;
		}
	}

	return false;
}

void solve() {
	memset(f, -1, sizeof f);
	memset(cnt, 0, sizeof cnt);
	int K;
	GI2(K, n); FI has[i].clear();
	f[(1 << n) - 1] = 0;
	REP(k, K) {
		int a; GI(a); ++cnt[a];
	}
	FI {
		GI(key[i]);
		GI(K); int a;
		REP(k, K) {
			GI(a); has[i].push_back(a);
		}
	}
	go(0);
}

int main() {
//freopen("input.txt", "rt", stdin);

freopen("D-small-attempt0.in", "rt", stdin);
freopen("D-small-attempt0.out", "w", stdout);
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		solve();
		printf("Case #%d:", tc);

		int mask = 0;
		if (f[mask] >= 0 ) {
			FI {
				printf(" %d", f[mask]+1);
				mask |= 1 << f[mask];
			}
			puts("");
		} else
			puts(" IMPOSSIBLE");
	}

}
