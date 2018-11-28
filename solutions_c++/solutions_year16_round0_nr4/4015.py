#include <stdio.h>

int main (void) {
	int t, cc;
	scanf ("%d", &t);
	for (cc = 1; cc <= t; cc++) {
		printf ("Case #%d:", cc);
		int k, c, s;
		scanf ("%d%d%d", &k, &c, &s);
		for (int i = 0; i < k; i++) {
			long long curr = i;
			long long len = k;
			for (int j = 1; j < c; j++) {
				curr = len * curr + i;
			}
			printf (" %lld", curr+1); 
		}
		printf ("\n");
	}
}
