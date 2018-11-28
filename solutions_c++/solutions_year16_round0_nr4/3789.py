#include <stdio.h>

int t, k, c, s;

int main()
{
	scanf("%d", &t);
	int j;
	for(j = 0; j < t; j++)
	{
		scanf("%d%d%d", &k, &c, &s);
		int i;
		printf("Case #%d: ", j + 1);
		for(i = 1; i <= k; i++)
			printf("%d%c", i, (i == k ? '\n' : ' '));
	}
	return 0;
}
