#include <stdio.h>

int main (void) {
	int v[4];
	int i, j, k;
	int x, tmp, r;
	int t, c;
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		printf ("Case #%d: ", c);
		scanf ("%d", &r);
		r--;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf ("%d", &tmp);
				if (i == r)	v[j] = tmp;
			}
		}
		int cnt = 0;
		scanf ("%d", &r);
		r--;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf ("%d", &tmp);
				if (i == r) {
					for (k = 0; k < 4; k++) {
						if (tmp == v[k]) {
							cnt++;
							x = v[k];
						}
					}
				}
			}
		}
		if (cnt == 0)	printf ("Volunteer cheated!\n");
		else if (cnt == 1)	printf ("%d\n", x);
		else	printf ("Bad magician!\n");
	}
	return 0;
}
