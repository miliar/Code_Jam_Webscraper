#include<stdio.h>

int Map[5][5]={{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}};

int A[100000], N;
int L, X;
char str[100000];
int R[100000];
int Ret;
int T;

int main(void)
{
	int l0, l1, l2;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &L, &X);
		N = L * X;
		scanf("%s", str);
		for(l1 = 0; l1 < L; l1++)
		{
			if(str[l1] == 'i') A[l1] = 2;
			else if(str[l1] == 'j') A[l1] = 3;
			else if(str[l1] == 'k') A[l1] = 4;
		}
		for(l1 = L; l1 < N; l1++) A[l1] = A[l1-L];

//		for(l1 = 0; l1 < N; l1++) printf("%d", A[l1]);
//		printf("\n");

		fprintf(stderr, "%d/%d %d %d %d\n", l0, T, L, X, N);

		Ret = 0;

		if(N >= 3)
		{
			int curr = 1;
			for(l1 = N-1; l1 >= 1; l1--)
			{
				if(curr < 0) curr = -Map[A[l1]][-curr];
				else curr = Map[A[l1]][curr];

				if(curr == 4) R[l1] = 1;
				else R[l1] = 0;
			}
			R[N] = 0;

			curr = 1;
			for(l1 = 0; l1+1 < N; l1++)
			{
				if(curr < 0) curr = -Map[-curr][A[l1]];
				else curr = Map[curr][A[l1]];

				if(curr == 2)
				{
					int curr2 = 1;
					for(l2 = l1+1; l2+1 < N; l2++)
					{
						if(curr2 < 0) curr2 = -Map[-curr2][A[l2]];
						else curr2 = Map[curr2][A[l2]];

						if(curr2 == 3 && R[l2+1])
						{
							Ret = 1;
							goto maki;
						}
					}
				}
			}
		}

maki:
		if(Ret) printf("Case #%d: YES\n", l0);
		else printf("Case #%d: NO\n", l0);
	}
}
