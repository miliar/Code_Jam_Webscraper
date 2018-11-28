#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int n, k, c, s;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < s; j++) {
			printf("%d", j + 1);
			if (j != s - 1) {
				printf(" ");
			}
		}
		printf("\n");
	}
}
