#include <cstdio>
#include <cstring>

const int maxn = 105;
char s[maxn];

int solve() {
	int ret = 0, l = strlen(s);
	char last = '+';
	for (int i=l-1;i>=0;i--) {
		if (s[i] != last) {
			ret ++;
			last = s[i];
		}
	}
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%s", s);
		int ans = solve();
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
