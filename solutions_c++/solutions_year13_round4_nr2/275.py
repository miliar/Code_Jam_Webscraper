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

int n;
LL p;

#define SET(w, b) ((w) & (1LL << (b)))

LL solve_max() {
	LL win= 0;
	int nwins = 0;
	int round = n-1;
	while(round >= 0 && !SET(p, round)) --round, ++nwins;
	bool has_wins = false;
	for (;round >=0; --round) if (!SET(p, round)) has_wins = true;

	nwins += has_wins;
	FIR(nwins) win = 1 + 2*win;
	return (1LL << n) - 1 - win;
}

int main() {
//freopen("input.txt", "rt", stdin);
freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);

	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		cin >> n >> p; --p;
		LL res_max = solve_max();

		LL res_g = (1LL << n) -1;
		if (p != (1LL << n) -1) {
			p = (1LL << n) -2 - p;
			res_g = (1LL << n) - 2- solve_max();
		}
		printf("Case #%d: ", tc);
		cout << res_g << " " << res_max << endl;
	}	
}
