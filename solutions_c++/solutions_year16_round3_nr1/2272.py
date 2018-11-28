#include <bits/stdc++.h>

using namespace std;

int i, t, j, k, l, num, f, sum, n, id[100], p[100], buf;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.ans", "w", stdout);
	
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &n);
		sum = 0;
		for (j = 0; j < n; j++) {
			scanf("%d", &p[j]);
			sum += p[j];
			id[j] = j;
		}
		
		printf("Case #%d: ", i + 1);
		
		for (num = sum; num > 0; num--) {
			for (j = 0; j < n; j++) {
				if (p[j] == 0)
					continue;
				p[j]--;
				f = 0;
				for (k = 0; k < n; k++)
					if (p[k] > ((num - 1) / 2)) {
						f = 1;
						break;
					}
		
				if (f) {
					p[j]++;
				} else {
					printf("%c ", j + 'A');
					break;
				}
			}
			
			if (f)
			for (j = 0; j < n; j++)
				for (k = j + 1; k < n; k++) {
					if (p[j] == 0 || p[k] == 0)
						break;
					p[j]--;
					p[k]--;
					f = 0;
					for (l = 0; l < n; l++)
						if (p[l] > ((num - 2) / 2)) {
							f = 1;
							break;
						}
					if (f) {
						p[j]++;
						p[k]++;
					} else {
						printf("%c%c ", j + 'A', k + 'A');
						num--;
						break;
					}
				}
					
// 		for (j = 0; j < n; j++)
// 			printf("%d ", p[j]);
// 		printf("\n");
		}
		
		printf("\n");
	}
	
	return 0;
}