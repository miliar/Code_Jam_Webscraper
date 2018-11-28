#include <cstdio>
#include <climits>

#include <algorithm>
using std::min;
using std::max;

const int MaxN = 111;
int n, m, h[MaxN][MaxN];

void input() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++ i) {
		for (int j = 0; j < m; ++ j)
			scanf("%d", &h[i][j]);
	}
}

bool solve() {
	int r[MaxN], c[MaxN];
	for (int i = 0; i < n; ++ i) r[i] = INT_MIN;
	for (int i = 0; i < m; ++ i) c[i] = INT_MIN;
	for (int i = 0; i < n; ++ i) {
		for (int j = 0; j < m; ++ j) {
			r[i] = max(r[i], h[i][j]);
			c[j] = max(c[j], h[i][j]);
		}
	}
	for (int i = 0; i < n; ++ i) {
		for (int j = 0; j < m; ++ j)
			if (h[i][j] != min(r[i], c[j])) return false;
	}
	return true;
}

int main() {
	int test_cases;
	scanf("%d", &test_cases);
	for (int t = 1; t <= test_cases; ++ t) {
		input();
		printf("Case #%d: %s\n", t, solve() ? "YES" : "NO");
	}
	return 0;
}
