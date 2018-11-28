//	Google Code Jam 2016 Round 1A
//	Problem A

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
	int n, m, k;
	//int e[maxN][maxN];
	//int e_n[maxN];
	char s[maxN];

public:
	Qs() {
		
	}

	bool input() {

		if (scanf("%s", s) != 1)
			return false;
		
		n = strlen(s);



		return true;
	}

	void solve() {

		string sol;
		sol += s[0];

		for (int i = 1; i < n; ++i) {
			// D("> i%d %c %c\n", i, sol[0], s[i]);
			if (s[i] >= sol[0]) {
				sol = s[i] + sol;
			} else {
				sol = sol + s[i];
			}
		}

		printf("Case #%d: %s\n", caseI, sol.c_str());



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
