#pragma comment(linker, "/stack:256000000")

#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <cassert>
#include <queue>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()

int a[111][111];
int n, m;

bool check() {
	REP(i, n) REP(j, m) {
		bool OK = 1;
		REP(k, m) {
			if (a[i][k] > a[i][j]) {
				OK = 0;
				break;
			}
		}
		if (OK) continue;
		REP(k, n) {
			if (a[k][j] > a[i][j]) {
				return 0;
			}
		}		
	}
	return 1;
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long start = clock();
#endif
	int tst;
	cin >> tst;
	for (int test = 1; test <= tst; test++) {
		printf("Case #%d: ", test);
		cin >> n >> m;
		REP(i, n) REP(j, m) cin >> a[i][j];
		puts(check()? "YES": "NO");		
	}
#ifdef LOCAL
	fprintf(stderr, "\n\nTime: %.3lf\n\n", (clock() - start) / 1000.);
#endif
	return 0;
}