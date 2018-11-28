#include <cstdio>
#include <algorithm>
using namespace std;

#define N (1 << 20)

int min(int a, int b) {
	return a < b ? a : b;
}

int max(int a, int b) {
	return a < b ? b : a;
}

int T, n, x, y;
long long p, q, r, s, d[N], ans, m, x1, x2, x3, t;

int main() {
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs) {
		printf("Case #%d: ", cs);
		scanf("%d%lld%lld%lld%lld", &n, &p, &q, &r, &s);
		d[0] = 0;
		for (int i = 0; i < n; ++i)
			d[i + 1] = (i*p + q)%r + s;
		for (int i = 1; i <= n; ++i)
			d[i] += d[i - 1];
		t = 0; x = 0; y = n; m = d[n]; ans = m;
		while (x <= y) {
			while (x <= n && d[x] <= t) ++x;
			while (0 <= y && m - d[y] <= t) --y;
			t = min(d[x], m - d[y]);
			if (d[x] <= t) x1 = d[x];
			else x1 = d[x - 1];
			if (m - d[y] <= t) x2 = m - d[y];
			else x2 = m - d[y + 1];
			x3 = m - x1 - x2;
			ans = min(ans, max(x1, max(x2, x3)));
		}
		printf("%.10f\n", 1. - 1.*ans/d[n]);
	}
	return 0;
}
