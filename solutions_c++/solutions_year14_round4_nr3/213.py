#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <algorithm>
#define MAXN 1005

using namespace std;

struct node
{
	int b, c;
};

int N, M;

int getNum(int x, int y, int dir)
{
	return ((x-1) * M + (y-1)) * 2 + dir;
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static char b[MAXN][MAXN];
	static int s[5*MAXN*MAXN];
	static int q[5*MAXN*MAXN];
	static int w[5*MAXN*MAXN];
	static struct node a[20*MAXN*MAXN];
	static int dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static char flag[5*MAXN*MAXN];
	for (iT = 0; iT < T; iT++)
	{
		memset(b,1,sizeof(b));
		int B;
		scanf("%d %d %d",&M,&N,&B);
		int i, j, d, x, y, num;
		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= M; j++)
			{
				b[i][j] = 0;
			}
		}
		int x0, y0, x1, y1;

		int z2;
		for (z2 = 0; z2 < B; z2++)
		{
			scanf("%d %d %d %d",&y0,&x0,&y1,&x1);
			x0++; y0++; x1++; y1++;
			for (i = x0; i <= x1; i++)
			{
				for (j = y0; j <= y1; j++)
				{
					b[i][j] = 1;
				}
			}
		}

		memset(s,0,sizeof(s));
		int S = getNum(N, M, 1) + 1;
		int T = getNum(N, M, 1) + 2;
		int V = getNum(N, M, 1) + 3;
		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= M; j++)
			{
				if (!b[i][j])
				{
					num = getNum(i, j, 1);
					for (d = 0; d < 4; d++)
					{
						x = i + dir[d][0];
						y = j + dir[d][1];
						if (!b[x][y])
						{
							s[num]++;
							s[getNum(x, y, 0)]++;
						}
					}
				}
			}
		}
		i = 1;
		for (j = 1; j <= M; j++)
		{
			if (!b[i][j])
			{
				s[S]++;
				s[getNum(i, j, 0)]++;
			}
		}
		i = N;
		for (j = 1; j <= M; j++)
		{
			if (!b[i][j])
			{
				s[T]++;
				s[getNum(i, j, 1)]++;
			}
		}
		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= M; j++)
			{
				if (!b[i][j])
				{
					s[getNum(i, j, 0)]++;
					s[getNum(i, j, 1)]++;
				}
			}
		}

		for (i = 1; i <= V; i++) s[i] += s[i-1];

		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= M; j++)
			{
				if (!b[i][j])
				{
					num = getNum(i, j, 1);
					for (d = 0; d < 4; d++)
					{
						x = i + dir[d][0];
						y = j + dir[d][1];
						if (!b[x][y])
						{
							s[num]--;
							a[s[num]].b = getNum(x, y, 0);
							a[s[num]].c = 0;
							s[getNum(x, y, 0)]--;
							a[s[getNum(x, y, 0)]].b = num;
							a[s[getNum(x, y, 0)]].c = 1;
						}
					}
				}
			}
		}
		i = 1;
		for (j = 1; j <= M; j++)
		{
			if (!b[i][j])
			{
				num = getNum(i, j, 0);
				s[S]--;
				a[s[S]].b = num;
				a[s[S]].c = 0;
				s[num]--;
				a[s[num]].b = S;
				a[s[num]].c = 1;
			}
		}
		i = N;
		for (j = 1; j <= M; j++)
		{
			if (!b[i][j])
			{
				num = getNum(i, j, 1);
				s[T]--;
				a[s[T]].b = num;
				a[s[T]].c = 1;
				s[num]--;
				a[s[num]].b = T;
				a[s[num]].c = 0;
			}
		}
		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= M; j++)
			{
				if (!b[i][j])
				{
					s[getNum(i, j, 0)]--;
					a[s[getNum(i, j, 0)]].b = getNum(i, j, 1);
					a[s[getNum(i, j, 0)]].c = 0;
					s[getNum(i, j, 1)]--;
					a[s[getNum(i, j, 1)]].b = getNum(i, j, 0);
					a[s[getNum(i, j, 1)]].c = 1;
				}
			}
		}

		//DO
		/*
		for (i = 0; i < V; i++)
		{
			printf("%2d:",i);
			for (j = s[i]; j < s[i+1]; j++) printf(" %2d (%2d)",a[j].b,a[j].c);
			printf("\n");
		}
		*/

		int res = 0;
		while (1)
		{
			memset(flag,0,sizeof(flag));
			int R = 0; int W = 1;
			q[R] = S;
			w[R] = -1;
			flag[S] = 1;
			while (W > R)
			{
				int point = q[R];
				if (point == T) break;
				for (i = s[point]; i < s[point+1]; i++)
				{
					if ((a[i].c < 1) && (!flag[a[i].b]))
					{
						q[W] = a[i].b;
						w[W] = R;
						flag[a[i].b] = 1;
						W++;
					}
				}
				R++;
			}
			if (W == R) break;
			j = R;
			while (j)
			{
				i = w[j];
				int p1 = q[i]; int p2 = q[j];
				int z;
				z = s[p1];
				while (a[z].b != p2) z++;
				a[z].c++;
				z = s[p2];
				while (a[z].b != p1) z++;
				a[z].c--;
				j = i;
			}

			//DO
			/*
			for (i = 0; i < V; i++)
			{
				printf("%2d:",i);
				for (j = s[i]; j < s[i+1]; j++) printf(" %2d (%2d)",a[j].b,a[j].c);
				printf("\n");
			}
			*/

			res++;
		}

		printf("Case #%d: %d\n",iT+1,res);
	}
	return 0;
}
