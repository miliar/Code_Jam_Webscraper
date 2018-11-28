#include <cstdio>
#include <algorithm>
using namespace std;

#define P 1000002013
#define N 1024

int T, n, m, a[N], b[N], d[N + N], dn, p[N], cn;
long long c[N + N], ini, fin;

long long cost(int a, int b) {
	return (d[b] - d[a])*(n + n - d[b] + d[a] + 1)/2;
}

long long solve(int x, int y) {
	if (y < x) return 0;
	int pmin = x;
	for (int i = x; i <= y; ++i)
		if (c[i] <= c[pmin]) pmin = i;
	int t = c[pmin];
	for (int i = x; i <= y; ++i)
		c[i] -= t;
	return (cost(x/2, y/2)*t%P + solve(x, pmin - 1) + solve(pmin + 1, y))%P;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < m; ++i) {
			scanf("%d%d%d", a + i, b + i, p + i);
			d[i + i] = a[i]; d[i + i + 1] = b[i];
		}
		dn = m + m;
		sort(d, d + dn);
		dn = unique(d, d + dn) - d;
		cn = dn + dn;
		for (int i = 0; i < cn; ++i)
			c[i] = 0;
		for (int i = 0; i < m; ++i) {
			a[i] = lower_bound(d, d + dn, a[i]) - d;
			b[i] = lower_bound(d, d + dn, b[i]) - d;
			c[a[i] + a[i]] += p[i];
			c[b[i] + b[i] + 1] -= p[i];
		}
		for (int i = 0; i < cn; ++i)
			c[i + 1] += c[i];
		for (int i = 0; i < cn; ++i)
			c[i] %= P;
		ini = 0;
		for (int i = 0; i < m; ++i)
			ini = (ini + cost(a[i], b[i])%P*p[i])%P;
		fin = solve(0, cn - 1);
		printf("%lld\n", (ini - fin + P)%P);
	}
	return 0;
}
