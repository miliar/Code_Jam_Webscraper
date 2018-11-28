#include <cstdio>
#include <algorithm>

using std::max;

const long long MAXN = 1000010;
long long n, p, q, r, s, M;
long long a[MAXN];

inline long long check(long long limit) {
	long long cnt = 1; long long sum = 0;
	for (long long i = 1; i <= n; i++) {
		if (sum + a[i] <= limit) sum += a[i]; else sum = a[i], cnt++;
	}
	return cnt <= 3;
}
int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	long long kase; scanf("%I64d", &kase); for (long long _ = 1; _ <= kase; _++) {
		scanf("%I64d%I64d%I64d%I64d%I64d", &n, &p, &q, &r, &s); M = 0;
		long long S = 0;
		for (long long i = 1; i <= n; i++) a[i] = ((long long)(i - 1) * p + q) % r + s, S += a[i], M = max(M, a[i]);
		long long l = M, r = S;
		while (l <= r) {
			long long mid = (l + r) >> 1;
			if (check(mid)) r = mid - 1; else l = mid + 1;
		}
		printf("Case #%I64d: %.10lf\n", _, (double) (S - l) / S);
	}
	return 0;
}

