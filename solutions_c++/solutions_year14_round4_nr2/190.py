#include <cstdio>

#define N (1 << 10)

int T, n, d[N], m, ans;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", d + i);
		ans = 0;
		while (n > 1) {
			m = 0;
			for (int i = 1; i < n; ++i)
				if (d[i] < d[m])
					m = i;
			for (int i = m; i + 1 < n; ++i)
				d[i] = d[i + 1];
			if (n - 1 - m < m)
				m = n - 1 - m;
			ans += m;
			--n;
		}
		printf("%d\n", ans);
	}
	return 0;
}
