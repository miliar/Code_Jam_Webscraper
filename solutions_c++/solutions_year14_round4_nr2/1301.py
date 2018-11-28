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

const int MAX = 1e3+10;
const int BARZYLION = 2e9;

int n;
pair<int, int> tab[MAX];

// {{ DRZ

const int DRZ = 1e3+10;

struct Drzewo {
	int drz[DRZ];

	Drzewo() {
		REP(i, DRZ) drz[i] = 0;
	}

	int magic(int x) {
		return x & (-x);
	}

	int update(int x) {
		while (x < DRZ) {
			drz[x]++;
			x += magic(x);
		}
	}

	int from0to(int x) {
		int ret = 0;
		while (x > 0) {
			ret += drz[x];
			x -= magic(x);
		}

		return ret;
	}

	int lessThan(int a) {
		return from0to(a-1);
	}

};

// }} DRZ

pair<int, int> tmp[MAX];

int check() {
	Drzewo d;
	int ret = 0;
	
	FORD(i, n-1, 0) {
		d.update(tmp[i].S);
		ret += d.lessThan(tmp[i].S);
	}

	return ret;
}

int solve(pair<int, int> m) {
	int ret = BARZYLION;

	REP(i, n) {
		int k = 0;
		REP(j, n) {
			if (k == i) {
				tmp[k++] = m;
			}
			if (tab[j] != m) {
				tmp[k++] = tab[j];
			}
		}
		if (k == i) {
			tmp[k++] = m;
		}

		sort(tmp, tmp+i);
		sort(tmp+i+1, tmp+n, greater<pair<int, int> >());

		/*REP(i, n) printf("%d ", tmp[i].S);
		printf("\t -> %d\n", check());
		*/
		ret = min(ret, check());
	}

	return ret;
}

int main() {
	int t, a;

	scanf("%d", &t);
	FOR(q, 1, t) {
		scanf("%d", &n);
		pair<int, int> m = MP(-1, -1);
		REP(i, n) {
			scanf("%d", &a);
			tab[i] = MP(a, i+1);
			m = max(tab[i], m);
		}

		printf("Case #%d: %d", q, solve(m));
		printf("\n");
	}

	return 0;
}
