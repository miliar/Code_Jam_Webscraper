#include <cstdio>

int main()
{
	int T;
	scanf("%d", &T);
	for(int caseno = 1; caseno <= T; caseno++)
	{
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d: ", caseno);
		if(K == S)
		{
			while(S)
			{
				printf("%d ", S);
				S--;
			}
			puts("");
		}
		else
		{
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
