#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int m, n;
	int a[102][102];
	int r[102], c[102];
	int i, j, t, f;
	int h = 1;
	scanf ("%d", &t);
	while (t--) {
		f = 0;
		scanf ("%d %d", &m, &n);
		for (i = 0; i < m; i++) {
			r[i] = 0;
		}
		for (i = 0; i < n; i++) {
        	       	c[i] = 0;
		}
		for (i = 0; i < m; i++) {
			for (j = 0; j < n; j++) {
				scanf ("%d", &a[i][j]);
				if (a[i][j] > r[i]) {
					r[i] = a[i][j];
				}
			}
		}
		for (i = 0; i < m; i++) {
                	for (j = 0; j < n; j++) {
                        	if (a[i][j] > c[j]) {
                        	       	c[j] = a[i][j];
                        	}
                	}
        	}
		for (i = 0; i < m; i++) {
                	for (j = 0; j < n; j++) {
				f = 0;
				if (a[i][j] < r[i] && a[i][j] < c[j]) {
					f = 1;
					break;
				}
               		}
			if (f) {
				break;
			}
        	}
		if (!f) {
			printf ("Case #%d: YES\n", h++);
		} else {
			printf ("Case #%d: NO\n", h++);
		}
	}
	return 0;
}
