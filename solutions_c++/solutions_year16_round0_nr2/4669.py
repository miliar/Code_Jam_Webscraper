#include <cstring>
#include <cstdio>

int T;
char s[109];

int main() {
	scanf("%d", &T);
	for (int iT = 1; iT <= T; ++iT) {
		printf("Case #%d: ", iT);
		scanf("%s", s);
		int ans = 0;
		int len = strlen(s);
		s[len] = '+';
		for (int i = 0; i < len; ++i) ans += s[i] != s[i+1];
		printf("%d\n", ans);
	}
	return 0;
}
