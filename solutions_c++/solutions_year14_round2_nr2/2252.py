#include <cstdio>

int main()
{
	int T, test, A, B , K, i, j, resp;

	scanf("%d", &T);
	for (test = 1; test <= T; test++)
	{
		scanf("%d", &A);
		scanf("%d", &B);
		scanf("%d", &K);

		resp = 0;

		for (i = 0; i < A; i++)
		{
			for (j = 0; j < B; j++)
			{
				if ((i & j) < K)
				{
					resp++;
				}
			}
		}

		printf("Case #%d: %d\n", test, resp);
	}

	return 0;
}
