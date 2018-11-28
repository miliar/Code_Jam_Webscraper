// Michał Łazowik

#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <utility>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

#define REP(x, n) for (int x = 0; x < n; ++x)
#define FOR(x, b, e) for (int x = b; x <= (e); ++x)
#define FORD(x, b, e) for (int x = b; x >= (e); --x)
#define FOREACH(it, cont) for (__typeof(cont.begin()) it = cont.begin(); it != cont.end(); ++it)

#define PB push_back
#define MP make_pair
#define F first
#define S second

const int MAX = 1e4+10;

int n, x, tab[MAX];

int solve() {
	int res = 0;

	sort(tab, tab+n);

	int l = 0, r = n-1;
	while (l <= r) {
		if (tab[l] + tab[r] <= x) {
			l++;
		}
		r--;
		res++;
	}

	return res;
}

int main() {
	int t;

	scanf("%d", &t);
	FOR(q, 1, t) {
		scanf("%d %d", &n, &x);
		REP(i, n) {
			scanf("%d", &tab[i]);
		}

		printf("Case #%d: %d", q, solve());
		printf("\n");
	}

	return 0;
}
