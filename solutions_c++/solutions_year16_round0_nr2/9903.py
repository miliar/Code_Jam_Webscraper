#include <stdio.h>
#include <string.h>

char s[102];

int main (void) {
	int t, c;
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		printf ("Case #%d: ", c);
		scanf ("%s", s);
		int len = strlen(s);
		s[len++] = '+';
		int ans = 0;
		char curr = s[0];
		for (int i = 0; i < len; i++) {
			if (s[i] != curr) {
				ans++;
				curr = s[i];
			}
		}
		printf ("%d\n", ans);
	}
	return 0;
}
