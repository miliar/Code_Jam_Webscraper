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
#define MAXN 64
//-----------------------------------------------------------
typedef struct OF {
	int j, p, s;
};

OF outfit[MAXN];
int tmpans[MAXN];
int ans[MAXN];
int J, P, S, K;
int comb, days;

bool check(int dep) {
	int cnt;
	for (int i = 0; i < dep; i++) {
		cnt = 0;
		for (int j = i + 1; j < dep; j++) {
			if (outfit[tmpans[i]].p == outfit[tmpans[j]].p &&
				outfit[tmpans[i]].s == outfit[tmpans[j]].s) {
				if (++cnt >= K) return false;
			}
		}
		cnt = 0;
		for (int j = i + 1; j < dep; j++) {
			if (outfit[tmpans[i]].j == outfit[tmpans[j]].j &&
				outfit[tmpans[i]].s == outfit[tmpans[j]].s) {
				if (++cnt >= K) return false;
			}
		}
		cnt = 0;
		for (int j = i + 1; j < dep; j++) {
			if (outfit[tmpans[i]].j == outfit[tmpans[j]].j &&
				outfit[tmpans[i]].p == outfit[tmpans[j]].p) {
				if (++cnt >= K) return false;
			}
		}
	}
	return true;
}

void find(int n, int dep) {
	if (comb + dep - n < days) return;
	if (n >= comb) {
		// Get an answer
		if (dep > days) {
			memcpy(ans, tmpans, sizeof(tmpans));
			days = dep;
		}
		return;
	}
	tmpans[dep] = n;
	if (check(dep + 1)) {
		find(n + 1, dep + 1);
	}
	find(n + 1, dep);
}

int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	scanf("%d", &cases);
	while (cases--) {
		scanf("%d%d%d%d", &J, &P, &S, &K);
		comb = 0;
		days = 0;

		printf("Case #%d: ", casenum++);

		// iteration all
		for (int i = 1; i <= J; i++) {
			for (int j = 1; j <= P; j++) {
				for (int k = 1; k <= S; k++) {
					outfit[comb].j = i;
					outfit[comb].p = j;
					outfit[comb].s = k;
					comb++;
				}
			}
		}
		// Find
		find(0, 0);
		// Ans
		printf("%d\n", days);
		for (int i = 0; i < days; i++) {
			printf("%d %d %d\n", outfit[ans[i]].j, outfit[ans[i]].p, outfit[ans[i]].s);
		}

		fflush(stdout);
	}
	return 0;
}
