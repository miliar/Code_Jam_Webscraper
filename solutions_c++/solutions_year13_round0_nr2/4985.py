#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN (1 << 7)
using namespace std;

int n, m;
int a[MAXN][MAXN];
int maxRow[MAXN], maxCol[MAXN];

inline void solve(int test) {
	bool ans = true;
	for (int i=0; i < n; ++i)
		for (int j=0; j < m; ++j) {
			maxRow[i] = max(maxRow[i], a[i][j]);
			maxCol[j] = max(maxCol[j], a[i][j]);
		}
	
	for (int i=0; i < n; ++i)
		for (int j=0; j < m; ++j)
			if (a[i][j] < maxRow[i] && a[i][j] < maxCol[j])
				ans = false;
	
	printf("Case #%d: %s\n", test, ans ? "YES" : "NO");
}

inline void read() {
	scanf("%d%d", &n, &m);
	
	for (int i=0; i < n; ++i)
		for (int j=0; j < m; ++j)
			scanf("%d", &a[i][j]);
}

inline void clear() {
	memset(maxRow, -1, sizeof(maxRow));
	memset(maxCol, -1, sizeof(maxCol));
	for (int i=0; i < MAXN; ++i)
		for (int j=0; j < MAXN; ++j)
			a[i][j] = 100;
}

int main() {
	int brt = 0, test = 0;
	scanf("%d", &brt);
	
	while (brt --) {
		clear();
		read();
		solve(++test);
	}
	return 0;
}