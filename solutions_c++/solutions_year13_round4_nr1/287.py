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

#define MOD 1000002013

int n, M;
LL dist[2010][2010];
int qs[2010], qe[2010];
LL cnt[2010];

int yy[2010];
LL r[2010];
LL e[2010];

typedef pair<PI, LL> PIL;

int solve() {	
	int N;
	GI2(N, M);
	FIR(M) {
		GI2(qs[i], qe[i]);
		cin >> cnt[i];
	}

	FIR(M) yy[2*i]=qs[i], yy[2*i+1]=qe[i];
	sort(yy, yy+2*M);
	int n = unique(yy, yy+2*M) - yy;
	memset(dist, 0, sizeof dist);

	FI FOR(j, i+1, n) {
		dist[i][j] = (LL)(yy[j]-yy[i])*(N+N-(yy[j]-yy[i])+1)/2;
		dist[i][j] %= MOD;
	}

	FIR(M) {
		qs[i]= lower_bound(yy, yy+n, qs[i]) - yy;
		qe[i]= lower_bound(yy, yy+n, qe[i]) - yy;
	}

	LL before = 0;
	FIR(M) {
		before += dist[qs[i]][qe[i]] * cnt[i] % MOD;
	}
	before %= MOD;

	memset(r, 0, sizeof r);
	memset(e, 0, sizeof e);
	FIR(M) {
		FOR(j, qs[i], qe[i])
			r[j] += cnt[i];
	}
	
	LL prev = 0;
	LL res = 0;
	FI {
		if (prev == r[i]) continue;
		if (prev < r[i]) {
			e[i] += r[i] - prev;
		} else {
			LL out = prev - r[i];
			FORD(j, i-1, 0) {
				LL take = min(out, e[j]);
				e[j] -= take;
				out -= take;
				res = (res + dist[j][i]*take) % MOD;
			}
		}
		prev = r[i];
	}

	res = (before - res) % MOD;
	if(res < 0) res += MOD;

	return res;
}

int main() {
//freopen("input.txt", "rt", stdin);
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		int res = solve();
		printf("Case #%d: %d\n", tc, res);
		cerr << res<< endl;
	}

}
