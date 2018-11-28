#include<stdio.h>
#include<string.h>
char s[1010];
int n, m;
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%s %d", s, &m);
		n = strlen(s);
		int ans = 0;
		for (int i = 0; i + m - 1 < n; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < m; j++) {
					s[i + j] = '-' ^ '+' ^ s[i + j];
				}
				ans++;
			}
		}
		int flag = 0;
		for (int i = 0; i < n; i++) {
			if (s[i] == '-')flag = 1;
		}
		if (flag == 0) {
			printf("Case #%d: %d\n", tc, ans);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", tc, ans);
		}
	}
	return 0;
}
