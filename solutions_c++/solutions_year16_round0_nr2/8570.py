#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	int t, n;
	freopen("B-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int a = 1; a <= t; a++) {
		char s[201];
		scanf("%s", s);
		int ans = 0, cnt = 0, leng = strlen(s);
		int m = 0, p = 0;
		for (int i = leng - 1; i >= 0; i--) {
			if (s[i] == '+') s[i] = 0;
			else break;
		}
		leng = strlen(s);
		int end = leng;
		while (1) {

			//printf("base : %s\n", s);
			int i;
			for (i = 0; i < leng; i++) {
				cnt++;
				if (m == 0 && p == 0) {
					if (s[i] == '+') p = 1;
					else m = 1;
				}
				else if (p == 1 && m == 0 && s[i] == '-') {
					ans++;
					//printf("---·Î\n");
					p = 0;
					m = 1;
				}
				else if (m == 1 && p == 0 && (i + 1 == leng || s[i] == '+')) {
					int k, c = 0;
					char tmp[101] = { 0, };
					for (k = leng - 1; k >= i; k--) {
						tmp[c++] = '+' + '-' - s[k];
					}
					tmp[c] = 0;
					strcpy(s, tmp);
					//printf("reverse : %s\n", s);
					ans++;
					m = p = 0;
					break;
				}
				if (m == 1 && i + 1 == leng) {
					ans++;
				}
			}
			//printf("%d %d\n", i, leng);
			if (i == leng)break;
			leng = strlen(s);
		}
		printf("Case #%d: %d\n", a, ans);
	}
	fclose(stdin);
	fclose(stdout);
}
