#include <stdio.h>

int T, K, C, S;

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(int cs = 1; cs <= T; cs++)
	{
		scanf("%d %d %d", &K, &C, &S);

		printf("Case #%d: ", cs);
		for(int i = 1; i <= S; i++)
		{
			printf("%d ", i);
		}
		printf("\n");
	}
	return 0;
}