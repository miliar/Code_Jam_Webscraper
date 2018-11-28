#include <stdio.h>
#include <stdlib.h>

void solve()
{
	int n;
	scanf("%d ", &n);
	int cur = 0;
	int sol = 0;

	for (int i = 0; i <= n; i++) {
		int a = getchar() - '0';
		if (cur < i) {
			sol += (i - cur);
			cur = i;
		}
		cur += a;
	}

	printf("%d\n", sol);
}

int main()
{
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
