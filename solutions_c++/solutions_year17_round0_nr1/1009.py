#include<stdio.h>
#include<string.h>
#pragma warning (disable:4996)

char str[10010];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int m, n, i, j, k, count = 0;
	int t, ti;
	scanf("%d", &t);
	for (ti = 0; ti < t; ti++) {
		count = 0;
		printf("Case #%d: ", ti + 1);
		scanf("%s %d", str, &k);
		n = strlen(str);
		for (i = 0; i < n - k + 1; i++) {
			if (str[i] == '-') {
				for (j = i; j < i + k; j++) {
					if (str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				count++;
			}
		}
		for (i = 0; i < n; i++) {
			if (str[i] == '-') {
				printf("IMPOSSIBLE\n");
				break;
			}
		}
		if (i == n) printf("%d\n", count);
	}
	return 0;
}