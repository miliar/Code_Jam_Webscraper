#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

const int MAX_N = 1010101;
lint a[MAX_N];
int n, p, q, r, s;
lint sum[MAX_N], ans;

bool gao(int b, int e) {
	lint x1 = sum[b - 1], x2 = sum[e] - sum[b - 1], x3 = sum[n] - sum[e];
	ans = min(ans, max(x1, max(x2, x3)));
	return x2 <= x3;
}

int main() {
	int n_case = 0;
	scanf("%d", &n_case);
	for (int ca = 1; ca <= n_case; ca++) {
		scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
		sum[0] = 0;
		for (int i = 1; i <= n; i++) {
			a[i] = (1LL * (i - 1) * p + q) % r + s;
			sum[i] = sum[i - 1] + a[i];
		}
		ans = sum[n];
		int b = 1, e = 1;
		while (b <= n) {
			while (e <= n && gao(b, e)) {
				e++;
			}
			gao(b, e - 1);
			b++;
		}
		lint d = __gcd(ans, sum[n]);
		ans /= d, sum[n] /= d;
		printf("Case #%d: %.12lf\n", ca, (sum[n] - ans) * 1.0 / sum[n]);
	}
	return 0;
}
