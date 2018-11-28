#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main (void) {
	int t, c, n, v[1000], i, j;
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		scanf ("%d", &n);
		for (i = 0; i < n; i++) {
			scanf ("%d", &v[i]);
		}
		int ans = 1001;
		for (i = 1; i < 1001; i++) {
			int curr = i;
			for (j = 0; j < n; j++) {
				if (v[j] > i) {
					curr += ((v[j] + i-1)/i)-1;
				}
			}
			ans = min(ans, curr);
		}
		printf ("Case #%d: %d\n", c, ans);
	}
}
