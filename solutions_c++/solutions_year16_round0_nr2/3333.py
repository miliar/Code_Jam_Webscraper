# include <stdio.h>
# include <stdlib.h>
# include <string.h>

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 0; kase < t; kase ++) {
		printf("Case #%d: ", kase + 1);

		char s[105];
		scanf("%s%*c", s);

		int i, j;
		i = j = 0;
		int n = strlen(s);

		int ans = 0;
		while (i < n) {
			while (j < n && s[j] == s[i]) j ++;
			if (j < n) ans ++; else {
				if (s[j - 1] == '-') {
					ans ++;
				}
			}

			i = j;
		}

		printf("%d\n", ans);
	}
}