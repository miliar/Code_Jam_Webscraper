#include<stdio.h>

int T, N, A[11111];
int Ret;

int main(void)
{
	int l0, l1, acc;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d", &N);
		acc = 0;
		Ret = 0;
		for(l1 = 0; l1 <= N; l1++)
		{
			scanf("%1d", &A[l1]);

			if(acc+Ret < l1)
			{
				Ret = l1 - acc;
			}
			acc += A[l1];
		}
		printf("Case #%d: %d\n", l0, Ret);
	}
	return 0;
}
