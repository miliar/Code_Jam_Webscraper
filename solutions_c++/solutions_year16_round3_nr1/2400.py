#include<stdio.h>
int t, n, N[26],sum,max,idx1,idx2,flag;
double check;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		scanf("%d", &n);
		sum = 0;
		for (int j = 0; j < n; j++) {
			scanf("%d", N + j);
			sum += N[j];
		}
		while (1) {
			max = 0;
			for (int j = 0; j < 26; j++) {
				if (N[j] > max) {
					max = N[j];
					idx1 = j;
				}
			}
			if (max == 0)break;
			N[idx1]--; sum--;
			flag = 0;
			for (int j = 0; j < 26; j++) {
				check = N[j] / (double)sum;
				if (check > 0.5) {
					flag = 1; break;
				}
			}
			if (flag) {
				max = 0;
				for (int j = 0; j < 26; j++) {
					if (N[j] > max) {
						max = N[j];
						idx2 = j;
					}
				}
				N[idx2]--; sum--;
				printf("%c%c ", 'A' + idx1, 'A' + idx2);
			}
			else printf("%c ", 'A' + idx1);
		}
		printf("\n");
	}
	return 0;
}