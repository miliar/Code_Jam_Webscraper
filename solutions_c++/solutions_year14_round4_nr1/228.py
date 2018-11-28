#include <cstdio>
#include <algorithm>
using namespace std;
#define N 12345

int t, n, x, ss[N]; char d[N];
int main() {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &n, &x);
		int ans = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", ss+i); d[i] = 0;
		}
		sort(ss, ss+n);
		for (int i = 0; i < n; i++) if (!d[i]) {
			ans++; d[i] = 1;
			int bst = i;
			for (int j = i+1; j < n; j++) if (!d[j] && ss[j] <= x - ss[i]) bst = j;
			d[bst] = 1;
		}
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}