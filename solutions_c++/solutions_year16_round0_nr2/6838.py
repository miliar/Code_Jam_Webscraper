#include <cstdio>
#include <cstring>
char s[110];
int main() {
	int t;
	int cnt;
	int n;
	int ans;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	cnt = 0;

	while (t--) {
		printf("Case #%d: ", ++cnt);
		ans = 0;
		scanf("%s", s);
		n = strlen(s);
		while (n--) if ((s[n] == '+' && (ans & 1)) || (s[n] == '-' && !(ans & 1))) ans++;
		printf("%d\n", ans);
	}
	return 0;
}