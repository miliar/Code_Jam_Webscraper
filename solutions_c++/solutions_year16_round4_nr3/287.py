#include <bits/stdc++.h>
#define MAXN 105

using namespace std;

static char res[MAXN][MAXN];

static int cur[MAXN];

static int endgoal[MAXN];
static int l[MAXN];
static int r[MAXN];

static int pairing[MAXN];

int connectBottom (int pos, int i, int N)
{
	if (i == 0)
	{
		if (res[pos][i] == '\\') return l[pos];
	}
	if (i == N-1)
	{
		if (res[pos][i] == '/') return r[pos];
	}
	if (res[pos][i] == '\\')
	{
		if (res[pos][i-1] == '\\') return -(i-1);
		else
		{
			if (cur[i-1] > 0) return cur[i-1];
			else return connectBottom(pos, -cur[i-1], N);
		}
	}
	else
	{
		if (res[pos][i+1] == '/') return -(i+1);
		else
		{
			if (cur[i+1] > 0) return cur[i+1];
			else return connectBottom(pos, -cur[i+1], N);
		}
	}
}

int connectTop (int pos, int i, int N)
{
	if (i == 0)
	{
		if (res[pos][i] == '/') return l[pos];
	}
	if (i == N-1)
	{
		if (res[pos][i] == '\\') return r[pos];
	}
	if (res[pos][i] == '/')
	{
		if (res[pos][i-1] == '/')
		{
			if (cur[i-1] > 0) return cur[i-1];
			else return connectBottom(pos, -cur[i-1], N);
		}
		else return -(i-1);
	}
	else
	{
		if (res[pos][i+1] == '\\')
		{
			if (cur[i+1] > 0) return cur[i+1];
			else return connectBottom(pos, -cur[i+1], N);
		}
		else return -(i+1);
	}
}

char solve (int pos, int max, int N)
{
	if (pos == max)
	{
		int i;
		for (i = 0; i < N; i++)
		{
			if (cur[i] > 0)
			{
				if (pairing[endgoal[i]] != cur[i]) return 0;
			}
			else
			{
				if (pairing[endgoal[i]] != endgoal[-cur[i]]) return 0;
			}
		}
		return 1;
	}
	else
	{
		/*printf("pos = %d\n",pos);
		for (int z = 0; z < N; z++) printf("%d ",cur[z]);
		printf("\n");*/

		int total = 1 << N;
		int bak[MAXN];
		for (int mask = 0; mask < total; mask++)
		{
			int i;
			int mask2 = mask;
			for (i = 0; i < N; i++)
			{
				if (mask2 % 2) res[pos][i] = '/';
				else res[pos][i] = '\\';
				mask2 /= 2;
			}

			//Checking for conflicts
			char isOK = 1;
			for (i = 0; i < N; i++)
			{
				if (cur[i] > 0)
				{
					int j = connectBottom(pos, i, N);
					if (j > 0)
					{
						if (pairing[cur[i]] != j)
						{
							isOK = 0;
							break;
						}
					}
				}
			}
			if (!isOK) continue;

			//Defining next row
			for (i = 0; i < N; i++)
			{
				bak[i] = connectTop(pos, i, N);
			}

			//Attempting it
			for (i = 0; i < N; i++)
			{
				int temp = bak[i]; bak[i] = cur[i]; cur[i] = temp;
			}
			if (solve(pos+1, max, N)) return 1;
			for (i = 0; i < N; i++)
			{
				int temp = bak[i]; bak[i] = cur[i]; cur[i] = temp;
			}

		}
		return 0;
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		int i, j;
		int R, C;
		scanf("%d %d",&R,&C);
		for (i = 0; i < 2*C+2*R; i+=2)
		{
			int x, y;
			scanf("%d %d",&x,&y);
			pairing[x] = y;
			pairing[y] = x;
		}
		printf("Case #%d:\n",iT+1);
		if (C <= R)
		{
			for (i = 0; i < C; i++)
			{
				endgoal[i] = i+1;
				cur[i] = 2 * C + R - i;
			}
			for (i = 0; i < R; i++)
			{
				r[R-i-1] = C+i+1;
				l[R-i-1] = 2*C + 2*R - i;
			}
/*
			printf("cur\n");
			for (i = 0; i < C; i++) printf("%d ",cur[i]);
			printf("\n");

			printf("endgoal\n");
			for (i = 0; i < C; i++) printf("%d ",endgoal[i]);
			printf("\n");

			printf("l[0] = %d\nr[0] = %d\n",l[0],r[0]);
*/
			if (solve(0, R, C))
			{
				for (i = R-1; i >= 0; i--)
				{
					for (j = 0; j < C; j++)
					{
						printf("%c",res[i][j]);
					}
					printf("\n");
				}
			}
			else printf("IMPOSSIBLE\n");
		}
		else
		{
			for (i = 0; i < R; i++)
			{
				endgoal[i] = 2*C + R + i + 1;
				cur[R-i-1] = C+i+1;
			}
			for (i = 0; i < C; i++)
			{
				r[C-i-1] = i+1;
				l[i] = C + R + i + 1;
			}
/*
			printf("cur\n");
			for (i = 0; i < R; i++) printf("%d ",cur[i]);
			printf("\n");

			printf("endgoal\n");
			for (i = 0; i < R; i++) printf("%d ",endgoal[i]);
			printf("\n");

			printf("l[0] = %d\nr[0] = %d\n",l[0],r[0]);
*/
			if (solve(0, C, R))
			{
				for (i = R-1; i >= 0; i--)
				{
					for (j = C-1; j >= 0; j--)
					{
						if (res[j][i] == '/') printf("\\");
						else printf("/");
					}
					printf("\n");
				}
			}
			else printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
