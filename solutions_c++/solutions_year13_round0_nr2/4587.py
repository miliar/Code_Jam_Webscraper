#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <sstream>
#include <numeric>
#include <climits>
#include <string>
#include <cctype>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

#define foreach(e, x) for (__typeof((x).begin()) e = (x).begin(); e != (x).end(); ++e)

const int MAX_N = 111;

int tests, n, m;
int h[MAX_N][MAX_N];
int row[MAX_N], column[MAX_N];

int main() {
	scanf("%d", &tests);
	for (int ctrl = 1; ctrl <= tests; ctrl++) {
		scanf("%d%d", &n, &m);
		fill(row, row + n, 0);
		fill(column, column + m, 0);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", h[i] + j);
				row[i] = max(row[i], h[i][j]);
				column[j] = max(column[j], h[i][j]);
			}
		}
		bool yes = true;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				yes &= min(row[i], column[j]) <= h[i][j];
			}
		}
		printf("Case #%d: %s\n", ctrl, yes ? "YES" : "NO");
	}
}

