#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t, n, m, i, j, k, f;
	int rsum[10], csum[10];
	scanf("%d", &t);

	for(i = 1; i <= t; i++) {
		scanf("%d %d", &n, &m);
		int a[n][m];

		for(j = 0; j < n; j++) {
			rsum[j] = 0;
			for(k = 0; k < m; k++) {
				scanf("%d", &a[j][k]);
				rsum[j] += a[j][k];
			}
		}

		for(k = 0; k < m; k++) {
			csum[k] = 0;
			for(j = 0; j < n; j++) {
				csum[k] += a[j][k];
			}
		}

		f = 0;
		for(j = 0; j < n; j++) {
			for(k = 0; k < m; k++) {
				if(a[j][k] == 1) {
				       	if(rsum[j] != m && csum[k] != n) {
						f = 1;
						break;
					}
				}
			}
		}

		if(f) {
			printf("Case #%d: NO\n", i);
		} else {
			printf("Case #%d: YES\n", i);
		}
	}

	return 0;
}
