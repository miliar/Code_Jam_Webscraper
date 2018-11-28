#include<stdio.h>


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int Tc = 1; Tc <= tc; Tc++) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d: ",Tc);
		for (int i = 1; i <= k; i++) {
			printf("%d ", i);
		}
		printf("\n");
	}
}