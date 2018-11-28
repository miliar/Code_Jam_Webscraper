#include <cstdio>
#include <cstring>

const int MAXN = 1005;
char s[MAXN];
int K;

int solve() {
	int N = strlen(s), ans = 0;
	for (int i = 0; i + K <= N; ++i) {
		if (s[i] == '-') {
			for (int j = 0; j < K; ++j)
				s[i + j] = (s[i + j] == '+') ? '-' : '+';
			++ans;
		}
	}
	for (int i = N - K + 1; i < N; ++i)
		if (s[i] == '-') return -1;
	return ans;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf(" %s%d", s, &K);
		printf("Case #%d: ", t);
		int ans = solve();
		if (ans < 0) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
