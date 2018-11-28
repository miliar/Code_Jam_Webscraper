#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 1;tc <= t;++tc) {
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ", tc);
		for (int i = 1;i <= k;++i)
			printf("%d ", i);
		printf("\n");
	}

	return 0;
}