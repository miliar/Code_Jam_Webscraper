#include <stdio.h>
#include <algorithm>

using namespace std;

int main (void) {
	int t, c, n, i, v[10000], j, mx;
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		int cnt = 0;
		scanf ("%d%d", &n, &mx);
		for (i = 0; i < n; i++)
			scanf ("%d", &v[i]);
		sort (v, v+n);
		i = 0;
		j = n-1;
		while (i < n && j >= i) {
			if (v[i] + v[j] <= mx) {
				i++; j--; cnt++;
			} else {
				j--; cnt++;
			}
		}
		printf ("Case #%d: %d\n",c, cnt);
	}
	return 0;
}
