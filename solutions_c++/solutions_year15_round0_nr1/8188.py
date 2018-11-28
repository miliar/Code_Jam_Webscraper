#include <bits/stdc++.h>

using namespace std;

#define gu getchar_unlocked()

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output1.ext", "w", stdout);
	int t, n, i, a, ans, k = 0;
	char s[10005];
	scanf("%d", &t);

	while (k++ < t) {
		scanf("%d", &n);
		scanf("%s", s);
		a = 0;
		ans = 0;
		for (i = 0; i <= n; i++) {
			if(s[i] != '0') {
				if (i <= a) {
					a += s[i]-48;
				} else {
					ans += i-a;
					a += s[i]-48+i-a;
				}
			}
		}
		printf("Case #%d: %d\n", k, ans);
	}
	fclose(stdout);
	return 0;
}
