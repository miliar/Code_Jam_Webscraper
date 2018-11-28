#include <bits/stdc++.h>
using namespace std;
void init_ios() {ios_base::sync_with_stdio(false); cin.tie(nullptr);}

void solve(int K, int C, int S) {
	if (S < K - C + 1) {
		puts(" IMPOSSIBLE");
		return;
	}

	long long k = 1;
	for (int i = 1; i < C; ++i) {
		k *= K;
	}

	for (int i = 0; i < S; ++i) {
		printf(" %lld", i * k + (k + 1) / 2);
	}

	puts("");
}

int main() {
	int T, K, C, S;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", i);
		solve(K, C, S);
	}
	return 0;
}
