#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);

	for (int u = 1; u <= t; u++) {
		int n;
		int m;
		scanf("%d%d", &n, &m);
		int a[n][m];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		
		int q = 0;
		int c;
		int d;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int p = a[i][j];
				c = 0;
				d = 0; 
				for (int w = 0; w < m; w++) {
					if (p >= a[i][w]) {
						c++;
					}
				}
				for (int w = 0; w < n; w++) {
					if (p >= a[w][j]) {
						d++;
					}
				}
				
				if (c != m && d != n) {
					printf("Case #%d: NO\n", u);
					q = 1;
					break;
				}
			}
			if (q == 1) {
				break;
			}
		}
		if (q == 0) {
			printf("Case #%d: YES\n", u);
		}
	}

	return 0;
}

