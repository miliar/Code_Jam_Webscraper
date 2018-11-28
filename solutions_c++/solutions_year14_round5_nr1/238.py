#include <cstdio>
#include <algorithm>
using namespace std;
#define N 1234567

int t, n, p, q, r, s; long long cum[N];
int main() {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
		for (int i = 1; i <= n; i++) cum[i] = ((i-1)*p+q)%r+s + cum[i-1];
		long long ans = cum[n];
		for (int st = 1, end = 1; st <= n; st++) {
			end = max(st, end);
			while (end < n && cum[end+1]-cum[st-1] <= cum[n]/3) end++;

			long long poss = cum[end]-cum[st-1];
			if (st > 1) poss = max(poss, cum[st-1]);
			if (end < n) poss = max(poss, cum[n] - cum[end]);
			ans = min(ans, poss);

			if (end != n) {
				poss = cum[end+1]-cum[st-1];
				if (st > 1) poss = max(poss, cum[st-1]);
				if (end+1 < n) poss = max(poss, cum[n] - cum[end+1]);
				ans = min(ans, poss);
			}
		}
		printf("Case #%d: %.10Lf\n", tc, 1.0 - ((long double)(ans))/cum[n]);
	}

	return 0;
}