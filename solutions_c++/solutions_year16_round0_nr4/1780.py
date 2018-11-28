#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <unistd.h>
#include <cassert>
#include <memory.h>
#include <limits>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

#define SMALL
//#define LARGE

int main() {
#ifdef SMALL
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("D-small-attempt3.txt", "w+", stdout);
//	freopen("input.in", "r", stdin);
//		freopen("output.txt", "w+", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w+", stdout);
#endif
	int TC;

	int k, c, s;
	scanf("%d", &TC);
	REP(t, TC)
	{
		scanf("%d%d%d", &k, &c, &s);
		if (t > 0) {
			printf("\n");
		}
		printf("Case #%d:", t + 1);

		if (k == 1) {
			printf(" %d", 1);
			continue;
		}

		if (c == 1) {
			if (s < k) {
				printf(" IMPOSSIBLE");
				continue;
			} else {
				for (int i = 1; i <= k; i++) {
					printf(" %d", i);
				}
				continue;
			}
		}

		if (k == 2) {
			if (s < 2) {
				printf(" IMPOSSIBLE");
			} else {
				printf(" %d", 2);
			}
			continue;
		}

		if (s >= k - 1) {
			long array[k];
			REP(i, k)
			{
				array[i] = i + 1;
			}
			for (int i = 2; i <= c; i++) {
				for (int j = 2; j < k; j++) {
					array[j] = array[j] + pow(k, i - 1) * (j - 1);
				}
			}
			for (int i = 1; i < k; i++) {
				printf(" %ld", array[i]);
			}
			continue;

		} else {
			printf("IMPOSSIBLE");
			continue;
		}
	}

	return 1;
}
