#include<stdio.h>

char A[1111];
int C[1111];
int T, N;

int main(void)
{
	int l0, l1, last, target;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%s", A);
		printf("Case #%d: ", l0);

		for(N = 0; A[N]; N++) C[N] = 0;
		
		last = N-1;
		while(1)
		{
			if(last == -1) break;
			target = last;
			for(l1 = last; l1 >= 0; l1--)
			{
				if(A[l1] > A[target]) target = l1;
			}
			printf("%c", A[target]);
			C[target] = 1;

			last = target - 1;
		}
		for(l1 = 0; l1 < N; l1++) if(C[l1] == 0) printf("%c", A[l1]);

		printf("\n");
	}

	return 0;
}
