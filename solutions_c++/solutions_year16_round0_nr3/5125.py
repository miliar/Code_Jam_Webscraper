#include <stdio.h>
#include <string.h>

const char one = '1';
const char zero = '0';

long long convert (char *s, int b) {
	long long ans = 0;
	int len = strlen(s);
	for (int i = 0; i < len; i++) {
		ans = ans * b + (s[i] == '1' ? 1 : 0);
	}
	return ans;
}

int main (void) {
	int t, c;
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		printf ("Case #%d:\n", c);
		int n, k;
		scanf ("%d%d", &n, &k);
		char s[33];
		for (int mask = 0; mask < k; mask++) {
			int m = mask;
			for (int i = 0; i < n; i++)	s[i] = zero;
			s[0] = s[n-1] = one;
			s[n] = '\0';
			int i = 1;
			while (m) {
				if (m&1) {
					s[i] = s[i+1] = one;
				}
				i+=2;
				m /= 2;
			}
			// for (int i = 2; i <= 10; i++) {
			// 	if (convert(s, i)%(i+1))	printf ("%d %lld NOOOO\n", i, convert(s, i));
			// }
			printf ("%s 3 4 5 6 7 8 9 10 11\n", s);
		}
	}
}
