#include <bits/stdc++.h>

using namespace std;

int i, j, n, t, k, l, a[10];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.ans", "w", stdout);
	
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &n);
		printf("Case #%d: ", i + 1);
		
		if (n == 0)
			printf("INSOMNIA\n");
		else {
			for (l = 0; l  < 10; l++) a[l] = 0;
			
			for (j = 1;; j++) {
				k = j * n;
				while (k > 0) {
					a[k % 10] = 1;
					k /= 10;
				}
				k = 0;
// 				for (l = 0; l < 10; l++)
// 					printf("%d ", a[l]);
// 				printf("\n");
				for (l = 0; l < 10; l++)
					if (a[l] == 0) {
						k = 1;
						break;
					}
				if (!k) {
					printf("%d\n", j * n);
					break;
				}
// 				if (j == 10)
// 					break;
			}
		}
	}
	
	return 0;
}