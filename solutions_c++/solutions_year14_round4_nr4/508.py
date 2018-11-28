#include<stdio.h>

char A[100][100];
char Str[100];
int Len;
int B[100];
int N, M;
int T;

int Child[1000][333];
int TN;

int Ret1, Ret2;

void Add(int curr, int idx)
{
	int l1;

	if(Str[idx] == 0) return;

	if(Child[curr][Str[idx] - 'A'] == 0)
	{
		Child[curr][Str[idx] - 'A'] = TN;
		for(l1 = 0; l1 < 26; l1++) Child[TN][l1] = 0;
		TN++;
	}

	Add(Child[curr][Str[idx] - 'A'], idx+1);
}

void Go(int Dep)
{
	if(Dep == N)
	{
		int l1, l2;

		for(l1 = 0; l1 < M; l1++)
		{
			for(l2 = 0; l2 < N; l2++)
			{
				if(B[l2] == l1) break;
			}
			if(l2 == N) return;
		}

		TN = 1;
		for(l1 = 0; l1 < 26; l1++) Child[0][l1] = 0;

		int nodes = 0;
		for(l1 = 0; l1 < M; l1++)
		{
			TN = 1;
			for(l2 = 0; l2 < 26; l2++) Child[0][l2] = 0;
			for(l2 = 0; l2 < N; l2++)
			{
				if(B[l2] != l1) continue;
				for(Len = 0; A[l2][Len]; Len++) Str[Len] = A[l2][Len];
				Str[Len] = 0;
				Add(0, 0);
			}
			nodes += TN;

			if(nodes > Ret1)
			{
				Ret1 = nodes;
				Ret2 = 1;
			}
			else if(nodes == Ret1)
			{
				Ret2++;
			}
		}
	}
	else
	{
		int l1;

		for(l1 = 0; l1 < M; l1++)
		{
			B[Dep] = l1;
			Go(Dep+1);
		}
	}
}

int main(void)
{
	int l0, l1, l2;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d", &N);
		scanf("%d", &M);
		for(l1 = 0; l1 < N; l1++) scanf("%s", A[l1]);

		Ret1 = -1;
		Ret2 = -1;

		Go(0);

		printf("Case #%d: %d %d\n", l0, Ret1, Ret2);
	}
}
