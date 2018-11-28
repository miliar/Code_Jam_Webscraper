#include <bits/stdc++.h>

using namespace std;

int T, K, C, S;
int main() {
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d: ", tt);
		long long ans = 1, delta = 1;
		for (int i = 1; i < C; i++) delta *= K;
		for (int i = 0; i < K; i++) {
			printf(" %I64d", ans);
			ans += delta;
		}
		puts("");
	}
	return 0;
}

