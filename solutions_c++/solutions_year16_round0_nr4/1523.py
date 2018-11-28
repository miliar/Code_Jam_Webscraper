#include<bits/stdc++.h>

int t, k, c, s, a;

int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", ++a);
		for (int i = 0; i < k; i++) printf(" %d", i + 1);
		printf("\n");
	}
	scanf("\n");
	return 0;
}
