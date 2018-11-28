#include <bits/stdc++.h>
using namespace std;
int A[1000005];
long long S[1000005];
int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		int N, p, q, r, s;
		scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);
		for (int i = 1; i <= N; ++i) {
			A[i] = (((long long)(i - 1) * p + q) % r) + s;
			S[i] = S[i - 1] + A[i];
		}
		long long ans = 1LL << 60;
		int pt = 0;
		for (int i = 1; i <= N; ++i) {
			long long rhs = S[N] - S[i];
			while (S[i] - S[pt + 1] >= S[pt + 1]) ++pt;
			ans = min(ans, max(rhs, max(S[pt], S[i] - S[pt])));
			if (pt + 1 < i) ans = min(ans, max(rhs, max(S[pt + 1], S[i] - S[pt + 1])));
		}
		printf("Case #%d: %.9lf\n", cn, double(S[N] - ans) / S[N]);
	}
}

