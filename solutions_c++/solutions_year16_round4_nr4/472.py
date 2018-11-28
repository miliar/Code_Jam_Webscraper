#include<stdio.h>

int N;
int A[111][111];
int B[111][111];
int C[111], CC[111];
int T;
int Ret;
int Fail;

void Go(int depth)
{
	int l1, l2;

	if(Fail) return;

	if(depth < N)
	{
		for(l1 = 0; l1 < N; l1++)
		{
			if(C[l1] == 1) continue;

			for(l2 = 0; l2 < N; l2++)
			{
				if(B[l1][l2] && CC[l2] == 0) break;
			}
			if(l2 == N)
			{
				Fail = 1;
				return;
			}

			C[l1] = 1;
			for(l2 = 0; l2 < N; l2++)
			{
				if(B[l1][l2] && CC[l2] == 0)
				{
					CC[l2] = 1;
					Go(depth + 1);
					CC[l2] = 0;
				}
			}
			C[l1] = 0;
		}
	}
}

int main(void)
{
	int l0, l1, l2, l3;
	int cnt;
	int curr;
	int flag;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d", &N);
		for(l1 = 0; l1 < N; l1++) for(l2 = 0; l2 < N; l2++) scanf("%1d", &A[l1][l2]);

		Ret = 0x7fffffff;
		for(flag = 0; flag < (1 << (N*N)); flag++)
		{
			l3 = 0;
			curr = 0;
			for(l1 = 0; l1 < N; l1++) for(l2 = 0; l2 < N; l2++)
			{
				B[l1][l2] = A[l1][l2];
				if(flag & (1 << l3))
				{
					B[l1][l2] = 1;
					if(A[l1][l2] == 0) curr++;
					else goto maki;
				}
				l3++;
			}
			if(curr >= Ret) goto maki;

			for(l1 = 0; l1 < N; l1++) C[l1] = 0;

			Fail = 0;
			Go(0);
			if(!Fail)
			{
				if(curr < Ret) Ret = curr;
			}

maki:
			continue;
		}

		printf("Case #%d: %d\n", l0, Ret);
	}
}
