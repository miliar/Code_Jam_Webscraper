#include <cstdio>

int main()
{
	int T, K, C, S,count=0;
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", ++count);
		for (int i = 1; i <= S; ++i) printf(" %d", i);
		putchar('\n');
	}
	return 0;
}