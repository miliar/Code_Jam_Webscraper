
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
#define MAXB 60
#define MAXE 100100
//-----------------------------------------------------------
ull B, M;
bool p[MAXB][MAXB];
ull ans;

struct E {
	int a, b;
};

E e[MAXE];
ull esize;

int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		memset(p, false, sizeof(p));
		memset(e, 0, sizeof(e));
		scanf("%llu%llu", &B, &M);
		printf("Case #%d: ", casenum++);
		if (((ull)1 << (B - 2)) < M) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		esize = 0;
		// Start to end
		e[esize].a = 0;
		e[esize].b = B - 1;
		esize++;
		M -= 1;
		for (ull i = 1; i < B; i++) {
			for (ull j = i + 1; j < B; j++) {
				e[esize].a = i;
				e[esize].b = j;
				esize++;
			}
		}

		for (ull i = 0; ((ull)1 << i) <= M; i++) {
			if (M & ((ull)1 << i)) {
				e[esize].a = 0;
				e[esize].b = B - i - 2;
				esize++;
			}
		}

		for (ull i = 0; i < esize; i++) {
			p[e[i].a][e[i].b] = true;
		}
		printf("POSSIBLE\n");
		for (ull i = 0; i < B; i++) {
			for (ull j = 0; j < B; j++) {
				printf("%d", (p[i][j]) ? 1 : 0);
			}
			printf("\n");
		}
		fflush(stdout);
	}
	return 0;
}

