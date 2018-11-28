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
	
	set<int> unseen;

public:
	Qs() {
		
	}

	bool input() {

		if (scanf("%d", &k) != 1)
			return false;
		
		unseen.clear();

		for (int i = 0; i < 10; ++i) {
			unseen.insert(i);
		}


		return true;
	}

	long long lastNum(int k) {
		// D("> starting with %d: remain %lu\n", k, unseen.size());

		if (k == 0) return -1;

		for (int i = 1; i <= 1000; ++i) {
			long long x = (long long)i * (long long)k;

			if (x == 0) {
				unseen.erase(0);
			} else for (long long p = x, j = 0; p > 0; p /= 10) {
				unseen.erase(p % 10);
			}

			// D(">> testing %lld: remain %lu\n", x, unseen.size());

			if (unseen.empty()) {
				D(">> found! count %d times\n", i);
				return x;
			}
		}
		return -1;
	}

	void solve() {

		/*for (int i = 0; i <= 100000; ++i) {
		
			unseen.clear();

			for (int i = 0; i < 10; ++i) {
				unseen.insert(i);
			}

			printf("%d > %lld\n", i, lastNum(i));
			fflush(stdout);
		}*/

		printf("Case #%d: ", caseI);

		long long sol = lastNum(k);

		if (sol == -1) {
			printf("INSOMNIA\n");
		} else {
			printf("%lld\n", sol);
		}



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
