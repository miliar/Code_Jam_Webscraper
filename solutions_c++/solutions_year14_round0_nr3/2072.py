//	Problem X

const bool debug=true;

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <utility>
#include <cassert>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>

#define TIMES(n) for (int i=0; i<(n); ++i)
#define FOR(i,s,t) for (int (i)=(s); (i)<=(t); ++(i))
#define RESET(a) memset((a), 0, sizeof((a)))
#define P(x, ...) printf((x), ##__VA_ARGS__)
#define D(x, ...) if (debug) printf((x), ##__VA_ARGS__)
#define MP(x, y) make_pair((x), (y))

const int INF = 0x7F7F7F7F; // or (unsigned)(-1)>>1
int caseI = 0, caseD = -1;

using namespace std;

//void P(char *f, ...) {va_list v; va_start(v, f); vprintf(f, v); va_end(v);}
//void D(char *f, ...) {if (!debug) return; va_list v; va_start(v, f); vprintf(f, v); va_end(v);}


/*

Sample Input:



Sample Output:


*/

const int maxN = 1005, maxM = 1005;

typedef pair<int, int> ii;
typedef vector<vector<ii> > graph;

class Qs {
	int n, m, t, k;
	char e[maxN][maxN];
	int spaces[maxN];

public:
	Qs() {
		RESET(spaces);
	}

	bool input() {

		if (scanf("%d%d%d", &n, &m, &t) != 3)
			return false;
		




		return true;
	}

	bool fillSpaces() {
		k = n * m - t;
		int kk = k;

		if (k < 1 || ((k == 2 || k == 3 || k == 5 || k == 7) && min(n, m) != 1)) {
			return false;
		} else if (k == 1) {
			spaces[0] = 1;
			return true;
		} else if (n == 1) {
			spaces[0] = k;
			return true;
		} else if (m == 1) {
			TIMES(k)
				spaces[i] = 1;
			return true;
		} else if ((k % 2 == 1 && min(n, m) == 2) || (k == 2 || k == 3 || k == 5 || k == 7)) {
			return false;
		}

		int i;
		for (i = 0; k > 0; ++i) {
			if (i < 2)
				spaces[i] = min(m, kk / 2);
			else
				spaces[i] = min(m, k);
			k -= spaces[i];
		}
		--i;
		if (spaces[i] == 1 && kk != 1) {
			int nn = (i == 2 ? 2 : 1);
			spaces[i] += nn;
			FOR(j, 1, nn)
				--spaces[i-j];
		}

		return true;
	}

	void solve() {

		printf("Case #%d:\n", caseI);

		if (!fillSpaces() || spaces[0] == 0) {
			printf("Impossible\n");
			return;
		}

		FOR(i, 0, n-1) {
			FOR(j, 1, spaces[i])
				if (i == 0 && j == 1)
					putchar('c');
				else
					putchar('.');
			FOR(j, spaces[i] + 1, m)
				putchar('*');
			putchar('\n');
		}

	}
};

void pre_process() {
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	scanf("%d", &caseD);
}

int main() {
	Qs *p = new Qs;
	pre_process();
	while ((++caseI|1) && caseD-- && p->input()) {
		p->solve();
		delete p;
		p = new Qs;
	}
	delete p;
	return 0;
}
