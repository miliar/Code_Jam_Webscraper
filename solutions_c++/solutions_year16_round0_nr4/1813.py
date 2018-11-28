#include <stdio.h>

int
main(void)
{
	int T, k;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d:", t);
		scanf("%d %*d %*d", &k);
		for(int i = 1; i <= k; i++)
			printf(" %d", i);
		printf("\n");
	}
}
