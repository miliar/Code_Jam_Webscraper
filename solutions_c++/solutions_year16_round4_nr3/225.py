#include<stdio.h>

int A[111][111];
int N, M, T;
int Label[1111], K;
int C[111][111][4];
int PX[1111], PY[1111], PZ[1111];
int Meet;
int CheckFlag;

void DFS(int me_x, int me_y, int me_z, const int you_x, const int you_y, const int you_z)
{
//	printf("%d %d %d / %d %d %d\n", me_x, me_y, me_z, you_x, you_y, you_z);
	if(me_x < 0 || me_x >= N || me_y < 0 || me_y >= M) return;

	if(C[me_x][me_y][me_z] == CheckFlag) return;
	C[me_x][me_y][me_z] = CheckFlag;

	if(Meet) return;
	if(me_x == you_x && me_y == you_y && me_z == you_z)
	{
		Meet = 1;
		return;
	}

	if(me_z == 0)
	{
		if(A[me_x][me_y] == 0)
		{
			DFS(me_x, me_y, 3, you_x, you_y, you_z);
		}
		else
		{
			DFS(me_x, me_y, 1, you_x, you_y, you_z);
		}
		DFS(me_x - 1, me_y, 2, you_x, you_y, you_z);
	}
	else if(me_z == 1)
	{
		if(A[me_x][me_y] == 0)
		{
			DFS(me_x, me_y, 2, you_x, you_y, you_z);
		}
		else
		{
			DFS(me_x, me_y, 0, you_x, you_y, you_z);
		}
		DFS(me_x, me_y + 1, 3, you_x, you_y, you_z);
	}
	else if(me_z == 2)
	{
		if(A[me_x][me_y] == 0)
		{
			DFS(me_x, me_y, 1, you_x, you_y, you_z);
		}
		else
		{
			DFS(me_x, me_y, 3, you_x, you_y, you_z);
		}
		DFS(me_x + 1, me_y, 0, you_x, you_y, you_z);
	}
	else if(me_z == 3)
	{
		if(A[me_x][me_y] == 0)
		{
			DFS(me_x, me_y, 0, you_x, you_y, you_z);
		}
		else
		{
			DFS(me_x, me_y, 2, you_x, you_y, you_z);
		}
		DFS(me_x, me_y - 1, 1, you_x, you_y, you_z);
	}
}

int main(void)
{
	int l0, flag, l1, l2, l3, l4;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		fprintf(stderr, "%d/%d..\n", l0, T);
		scanf("%d %d", &N, &M);
		K = N + M + N + M;
		for(l1 = 0; l1 < K; l1++)
		{
			scanf("%d", &Label[l1]);
			Label[l1]--;
		}

		l2 = 0;
		for(l1 = 0; l1 < M; l1++)
		{
			PX[l2] = 0;
			PY[l2] = l1;
			PZ[l2] = 0;
			l2++;
		}
		for(l1 = 0; l1 < N; l1++)
		{
			PX[l2] = l1;
			PY[l2] = M-1;
			PZ[l2] = 1;
			l2++;
		}
		for(l1 = M-1; l1 >= 0; l1--)
		{
			PX[l2] = N-1;
			PY[l2] = l1;
			PZ[l2] = 2;
			l2++;
		}
		for(l1 = N-1; l1 >= 0; l1--)
		{
			PX[l2] = l1;
			PY[l2] = 0;
			PZ[l2] = 3;
			l2++;
		}
		if(l2 != K)
		{
//			fprintf(stderr, "??\n");
		}
//		for(l1 = 0; l1 < K; l1++) printf("[%d %d %d]", PX[l1], PY[l1], PZ[l1]);

		for(flag = (1 << (N*M)) - 1; flag >= 0; flag--)
		{
			l3 = 0;
			for(l1 = 0; l1 < N; l1++) for(l2 = 0; l2 < M; l2++)
			{
				if(flag & (1 << l3)) A[l1][l2] = 1;
				else A[l1][l2] = 0;
				l3++;
			}
			
//			if(A[0][0] != 0 && A[0][1] != 0 && A[0][2] != 1) continue;
//			printf("!!!\n");

			Meet = 0;
			CheckFlag++;
			for(l1 = 0; l1 < K; l1+= 2)
			{
				Meet = 0;
				DFS(PX[Label[l1]], PY[Label[l1]], PZ[Label[l1]], PX[Label[l1+1]], PY[Label[l1+1]], PZ[Label[l1+1]]);
				if(Meet == 0)
				{
					break;
				}
			}
			if(l1 >= K)
			{
				goto maki;
			}
		}

		printf("Case #%d:\n", l0);
		printf("IMPOSSIBLE\n");
		continue;
maki:
		printf("Case #%d:\n", l0);
		for(l1 = 0; l1 < N; l1++)
		{
			for(l2 = 0; l2 < M; l2++)
			{
				if(A[l1][l2] == 1) printf("\\");
				else printf("/");
			}
			printf("\n");
		}
	}

	return 0;
}
