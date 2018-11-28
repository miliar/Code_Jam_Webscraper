#include<stdio.h>

int A[10001], C[10001], N;
int X;
int T;
int Ret;

int main(void)
{
	int l0, l1;
	int l2;

	scanf("%d", &T);

	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &N, &X);

		for(l1 = 1; l1 <= N; l1++)
		{
			scanf("%d", &A[l1]);
			C[l1] = 0;
		}

		for(l1 = 1; l1 <= N; l1++)
		{
			for(l2 = l1+1; l2 <= N; l2++)
			{
				if(A[l1] < A[l2])
				{
					int temp = A[l1];
					A[l1] = A[l2];
					A[l2] = temp;
				}
			}
		}

		Ret = 0;
		for(l1 = 1; l1 <= N; l1++)
		{
			if(C[l1]) continue;
			C[l1] = 1;
			for(l2 = l1+1; l2 <= N; l2++)
			{
				if(C[l2]) continue;
				if(A[l1] + A[l2] <= X)
				{
					C[l2] = 1;
					break;
				}
			}
			Ret++;
		}

		printf("Case #%d: %d\n", l0, Ret);
	}
	return 0;
}
