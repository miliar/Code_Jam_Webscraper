//	Google Code Jam 2015
//	Qualification Round
//	Problem A

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
	int a[maxN];

public:
	Qs() {
		
	}

	bool input() {

		if (scanf("%d ", &n) != 1)
			return false;
		
		m = 0;
		TIMES(n+1) {
			char c = getchar();
			a[i] = c - '0';
			m += a[i];
		}



		return true;
	}

	void solve() {

		k = 0;
		for (int i = 0, t = 0; m > 0; ++i) {
			if (a[i] > 0 && t < i) {
				k += i - t;
				t = i;
			}
			t += a[i];
			m -= a[i];
		}

		P("Case #%d: %d\n", caseI, k);

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
