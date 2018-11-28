#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
char s[N];
int main() {
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --) {
		int m;
		scanf("%s%d", s, &m);
		int n = (int) strlen(s), ans = 0;
		for (int i = 0; i <= n - m; ++ i) {
			if (s[i] == '-') {
				ans ++;
				for (int j = 0; j < m; ++ j) {
					s[i + j] = s[i + j] == '+' ? '-' : '+';
				}
			}
		}
		for (int i = 0; i < n; ++ i) if (s[i] != '+') ans = -1;
		printf("Case #%d: ", ++ zzz);
		if (ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
	}
}

