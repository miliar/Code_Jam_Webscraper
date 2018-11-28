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

typedef pair<int, char> gp;

struct CompareOrder {
    bool operator()(gp const& a, gp const& b) const {
        return a.first > b.first || (a.first == b.first && a.second < b.second);
    }
};

class Qs {
	int n, m, k;
	int a[maxN];
	priority_queue<gp> q;

public:
	Qs() {
		RESET(a);
	}

	bool input() {

		if (scanf("%d", &n) != 1)
			return false;
		
		int t;
		TIMES(n) {
			scanf("%d", &t);
			a['A' + i] = t;
		}



		return true;
	}

	void solve() {

		FOR(i, 'A', 'Z') {
			if (a[i] > 0) {
				q.push(MP(a[i], i));
			}
		}

		printf("Case #%d:", caseI);

		while (!q.empty()) {
			gp g1 = q.top(); q.pop();
			// D(" [%c/%d]", g1.second, g1.first);
			if (q.empty()) { // 1 gp remain
				TIMES(g1.first) {
					printf(" %c", g1.second);
				}
			} else { // at least 2 gp remain
				gp g2 = q.top();
				if (g1.first > g2.first) {
					printf(" %c", g1.second);
					if (--g1.first > 0) q.push(g1);
				} else {
					q.pop();
					if (!q.empty() && q.top().first == g2.first) { // g1 == g2 == g3
						printf(" %c", g1.second);
						if (--g1.first > 0) q.push(g1);
						q.push(g2);
					} else {
						printf(" %c%c", g1.second, g2.second);
						if (--g1.first > 0) q.push(g1);
						if (--g2.first > 0) q.push(g2);
					}
				}
			}
		}

		P("\n");

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
