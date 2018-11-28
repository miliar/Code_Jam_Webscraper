#include <bits/stdc++.h>
using namespace std;

int N;
int P[26];

bool loop() {
	for (int i = 0; i < N; ++i) if (P[i]) return true;
	return false;
}

int get_max() {
	int ret = 0;
	for (int i = 0; i < N; ++i) ret = max(ret, P[i]);
	return ret;
}

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) scanf("%d", P+i);

	while (loop()) {
		int maxi = get_max(), c;
		if (count(P, P+N, maxi) & 1) c = 1; else c = 2;
		putchar(' ');
		for (int i = 0; i < N; ++i) {
			if (P[i] != maxi) continue;
			--P[i];
			putchar('A'+i);
			if (!--c) break;
		}
	}

	puts("");
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d:", i);
		solve();
	}
	return 0;
}
