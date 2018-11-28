#include <cstdio>

char s[1005];

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ++ca){
		int n;
		scanf("%d%s", &n, s);
		int ans = 0, stand = 0;
		for (int i = 0; i <= n; ++i) {
			if (stand < i) {
				ans += i - stand;
				stand = i;
			}
			stand += s[i] - '0';
		}
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}

