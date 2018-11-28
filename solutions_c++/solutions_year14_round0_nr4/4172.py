/*
 * Michał Łazowik
 *
 * Google Code Jam 2014
 * Qualification Round
 * Problem D. Deceitful War
 *
 */

#include <cstdio>
#include <algorithm>

using namespace std;

#define REP(x, n) for (int x = 0; x < n; ++x)
#define FOR(x, b, e) for (int x = b; x <= (e); ++x)
#define FORD(x, b, e) for (int x = b; x >= (e); --x)

const int MAX = 1e3+10;
const double EPS = 1e-7;

int n;
double naomi[MAX], ken[MAX];

int war() {
	int kenDown = 0, kenUp = n-1, res = 0;
	FORD(i, n-1, 0) {
		if (ken[kenUp] > naomi[i]) {
			kenUp--;
		} else {
			res++;
			kenDown++;
		}
	}

	return res;
}

int deceitfulWar() {
	int kenDown = 0, kenUp = n-1, res = 0;
	REP(i, n) {
		if (naomi[i] > ken[kenDown]) {
			kenDown++;
			res++;
		} else {
			kenUp--;
		}
	}

	return res;
}

int main() {
	int q;
	
	scanf("%d", &q);

	FOR(i, 1, q) {
		scanf("%d", &n);
		REP(j, n) {
			scanf("%lf", &naomi[j]);
		}
		REP(j, n) {
			scanf("%lf", &ken[j]);
		}

		sort(naomi, naomi+n);
		sort(ken, ken+n);

		printf("Case #%d: %d %d\n", i, deceitfulWar(), war());
	}

	return 0;
}
