#include <cstdio>
#include <algorithm>
using namespace std;

#define N (1 << 14)

int T, n, c, d[N], t, ans;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &c);
		for (int i = 0; i < n; ++i)
			scanf("%d", d + i);
		sort(d, d + n);
		t = 0; ans = 0;
		for (int i = n - 1; i >= t; --i) {
			if (d[i] + d[t] <= c)
				++t;
			++ans;
		}
		printf("%d\n", ans);
	}
	return 0;
}
