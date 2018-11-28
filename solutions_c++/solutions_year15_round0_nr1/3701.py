#include <stdio.h>

int main (void) {
	int t, c, n, curr, i, ans;
	char s[1002];
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		scanf ("%d%s", &n, s);
		curr = ans = 0;
		for (i = 0; i <= n; i++) {
			if (s[i] != '0' && curr < i) {
				ans += i-curr;
				curr = i;
			}
			curr += s[i]-'0';
		}
		printf ("Case #%d: %d\n", c, ans);
	}
}
