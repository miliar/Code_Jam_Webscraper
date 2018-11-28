//#pragma warning( disable : 4996 )
#include<stdio.h>

int A, B, K;
int i, j, x;
int res, test;

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	scanf("%d", &test);
	for (x = 1; x <= test; x++)
	{
		res = 0;
		scanf("%d %d %d", &A, &B, &K);
		for (i = 0; i < A; i++)
		{
			for (j = 0; j < B; j++)
				if ((i & j) < K) res++;
		}
		printf("Case #%d: %d\n", x, res);
	}
	return 0;
}