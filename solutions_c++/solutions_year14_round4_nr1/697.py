#include <cstdio>
#include <algorithm>

int a[101010];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int qwe;
	scanf("%d", &qwe);
	for (int t = 1; t <= qwe; t++) {
		printf("Case #%d: ", t);
		int n, x;
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		std::sort(a, a + n);
		int ans = 0;
		for (int i = 0, j = n - 1; i <= j; ans++) {
			if (i == j)
				j--;
			else
				if (a[i] + a[j] > x)
					j--;
				else{
					i++;
					j--;
				}
		}
		printf("%d\n", ans);
	}
	return 0;
}
