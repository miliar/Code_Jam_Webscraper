#include <cstdio>

#define N 1024
#define M 128

int T, n, m, k;
long long d[N], mn[M], mx[M], sum[M], s, t;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n - m + 1; ++i)
			scanf("%lld", d + i);
		for (int i = 0; i < m; ++i)
			mn[i] = mx[i] = sum[i] = 0;
		for (int i = 0; i < n - m; ++i) {
			k = i%m;
			sum[k] += d[i + 1] - d[i];
			if (mn[k] > sum[k]) mn[k] = sum[k];
			if (mx[k] < sum[k]) mx[k] = sum[k];
		}
		for (int i = 0; i < m; ++i) {
			mx[i] -= mn[i];
			d[0] += mn[i];
		}
		d[0] = (d[0]%m + m)%m;
		s = t = 0;
		for (int i = 0; i < m; ++i)
			if (s < mx[i]) s = mx[i];
		for (int i = 0; i < m; ++i)
			t += s - mx[i];
		printf("%lld\n", s + (d[0] > t));
	}
	return 0;
}
