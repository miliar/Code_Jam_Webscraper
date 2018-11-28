#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main ()
{

	int t;
	scanf ("%d", &t);

	int cas = 0;
	while (t--) {
p:
		int r, c, j;
		scanf ("%d %d", &r, &c);
		int i;
		int a[r][c], b[r][c];
		for (i = 0; i < r; i++) {
			for (j = 0; j < c; j++) {
				scanf ("%d", &a[i][j]);
				b[i][j] = 100;
			}
		}

		int ro[r], col[c];
		for (i = 0; i < r; i++) {
			ro[i] = *max_element (a[i], a[i] + c);

			for (j = 0; j < c; j++) {
				if (b[i][j] > ro[i]) {
					b[i][j] = ro[i];
				}
			}
		}

		int max = 0;
		for (i = 0; i < c; i++) {
			max = 0;
			for (j = 0; j < r; j++) {
				if (max < a[j][i]) {
					max = a[j][i];
				}
			}
			for (j = 0; j < r; j++) {
				if (b[j][i] > max) {
					b[j][i] = max;
				} 
			}
		}

		int flag = 0;
		printf ("Case #%d: ", ++cas);
		for (i = 0; i < r; i++) {
			for (j = 0; j < c; j++) {
				if (a[i][j] != b[i][j]) {
					printf ("NO\n");
					flag = 1;
					break;
				}
			}
			if (flag == 1) {
				break;
			}
		}
		if (flag == 0) 	printf ("YES\n");
	}
	return 0;
}
