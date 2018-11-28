#include <bits/stdc++.h>

using namespace std;

int main()
{
	int i, j, k, c, s, t;
	
	freopen("d.in", "r", stdin);
	freopen("d.ans", "w", stdout);
	
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d%d%d", &k, &c, &s);
		if (s == k) {
			printf("Case #%d:", i + 1);
			for (j = 1; j <= k; j++)
				printf(" %d", j);
			printf("\n");
		}
	}
	
	return 0;
}