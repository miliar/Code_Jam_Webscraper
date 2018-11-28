#include <cstdio>

int main() {
	int T, S;
	char s[1005];
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%s", &S, s);
		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= S; ++i) {
			if (sum < i) {
				ans += (i - sum);
				sum = i;
			}
			sum += (s[i] - '0');
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}