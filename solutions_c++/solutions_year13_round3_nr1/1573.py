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
#define REPE(i,s,t) for (int (i)=(s); (i)<=(t); ++(i))
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

const int maxN = 1000005, maxM = 1005;

typedef pair<int, int> ii;
typedef vector<vector<ii> > graph;

class Qs {
	int n, m, k;
	char s[maxN];
	bool a[maxN];
	int b[maxN];
	//int e[maxN][maxN];
	//int e_n[maxN];

public:
	Qs() {
		
	}

	bool input() {

		if (scanf("%s%d", s, &n) != 2)
			return false;
		
		m = strlen(s);



		return true;
	}

	void solve() {

		TIMES(m) {
			a[i] = s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u';
			// D(">> [%d] = %d\n", i, a[i]);
		}

		long long int count = 0;
		int last = 0, sum;

		REPE(i, 0, m-1) {
			// int k = lower_bound(b, b+m, n+last);
			// if (k)


			// last = a[i];

			sum = 0;
			REPE(j, i, m-1) {
				//b[j] = (j>0? b[j-1]: 0) + a[j];
				if (a[j])
					++sum;
				else
					sum = 0;
				// D(">> (%d, %d) = %d\n", i, j, sum);
				if (sum >= n) {
					count += m-j;
					break;
				}
			}
		}

		P("Case #%d: %d\n", caseI, count);

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
