//	Problem X

const bool debug=false;

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
	int n, m, k;
	//int e[maxN][maxN];
	//int e_n[maxN];
	bool a[maxN];
	char s[maxN];



public:
	Qs() {
		
	}

	bool input() {

		if (scanf("%s", s) != 1)
			return false;
		
		n = strlen(s);
		TIMES(n) {
			a[i] = (s[i] == '+');
		}



		return true;
	}

	void flip(bool *a, int start_inclusive, int end_inclusive) {
		int len = end_inclusive - start_inclusive + 1;
		if (len % 2 == 1) {
			a[start_inclusive + len / 2] ^= true;
		}
		for (int i = len / 2 - 1; i >= 0; --i) {
			bool tmp = a[end_inclusive - i];
			a[end_inclusive - i] = !a[start_inclusive + i];
			a[start_inclusive + i] = !tmp;
		}
	}

	int findFirst(bool *a, bool target, int start, int end_exlusive, int direction) {
		for (int i = start; i != end_exlusive; i += direction) {
			if (a[i] == target) {
				return i;
			}
		}
		return -1;
	}

	int greedy() {
		bool b[maxN];
		copy(begin(a), end(a), begin(b));

		int last0 = n-1, nRound = 0;
		bool found;

		for (nRound = 0; (last0 = findFirst(b, false, last0, -1, -1)) >= 0; ++nRound) {
			D(">> r%d: last0 = %d ", nRound, last0);
			TIMES(n) D("%c", b[i] ? '+' : '-');
			D("\n");
			int lo = 0, hi = n-1;
			if (b[0]) { // if start with +
				// find first -
				hi = findFirst(b, false, 1, last0 + 1, 1);
				// if (hi != -1) {
				flip(b, lo, hi - 1);
				// } else {
					// break;
				// }
			} else { // if start with -
				// flip between -......-
				flip(b, lo, last0);
			}
		}
		return nRound;
	}


	void solve() {

		printf("Case #%d: %d\n", caseI, greedy());


	}
};

void pre_process() {
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	scanf("%d%*c", &caseD);
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
