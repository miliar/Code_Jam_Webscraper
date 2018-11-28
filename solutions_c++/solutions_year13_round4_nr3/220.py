#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 2005

using namespace std;

static char flag[MAXN];
int countf;
static int g[MAXN][MAXN];
int N;

void DFS (int point)
{
	flag[point] = 1;
	countf++;
	int i;
	for (i = 0; i < N; i++)
	{
		if ((g[i][point] == 1) && (!flag[i]))
		{
			DFS(i);
		}
	}
}

void DFS2 (int point)
{
	flag[point] = 1;
	countf++;
	int i;
	for (i = 0; i < N; i++)
	{
		if ((g[i][point] == -1) && (!flag[i]))
		{
			DFS2(i);
		}
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static int a[MAXN];
	static int b[MAXN];
	for (iT = 0; iT < T; iT++)
	{
		printf("Case #%d:",iT+1);
		memset(g,0,sizeof(g));
		scanf("%d",&N);
		int i;
		for (i = 0; i < N; i++) scanf("%d",&(a[i]));
		for (i = 0; i < N; i++) scanf("%d",&(b[i]));
		int j;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < i; j++)
			{
				if (a[j] >= a[i])
				{
					g[i][j] = 1;
					g[j][i] = -1;
				}
			}
			j = i-1;
			while ((j >= 0) && ((a[j] + 1) != a[i])) j--;
			if (j >= 0)
			{
				g[j][i] = 1;
				g[i][j] = -1;
			}
		}
		for (i = N-1; i >= 0; i--)
		{
			for (j = i+1; j < N; j++)
			{
				if (b[j] >= b[i])
				{
					g[i][j] = 1;
					g[j][i] = -1;
				}
			}
			j = i+1;
			while ((j < N) && ((b[j] + 1) != b[i])) j++;
			if (j < N)
			{
				g[j][i] = 1;
				g[i][j] = -1;
			}
		}
		/*printf("\n");
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N; j++)
			{
				if (g[i][j] > 0) printf("+");
				else if (g[i][j] < 0) printf("-");
				else printf(".");
			}
			printf("\n");
		}*/
		static int res[MAXN];
		static char used[MAXN];
		static int min[MAXN];
		static int max[MAXN];
		memset(used,0,sizeof(used));
		memset(res,0,sizeof(res));
		memset(min,0,sizeof(min));
		memset(max,0,sizeof(max));
		for (i = 0; i < N; i++)
		{
			memset(flag,0,sizeof(flag));
			countf = 0;
			DFS(i);
			min[i] = countf;
			memset(flag,0,sizeof(flag));
			countf = 0;
			DFS2(i);
			max[i] = N - countf + 1;
		}
		/*for (i = 0; i < N; i++)
		{
			j = min[i];
			while (used[j]) j++;
			res[i] = j;
			used[j] = 1;
		}*/

		static pair<int, char> ev[2*MAXN];
		int evc;
		for (i = 0; i < N; i++)
		{
			evc = 0;
			for (j = i+1; j < N; j++)
			{
				ev[evc] = make_pair(min[j], 'i');
				evc++;
				ev[evc] = make_pair(max[j], 'o');
				evc++;
			}
			sort(ev,ev+evc);

			for (j = min[i]; j <= max[i]; j++)
			{
				if (!used[j])
				{
					used[j] = 1;
					char good = 1;
					int seg = 0;
					int goodseg = 0;
					int k;
					int pos = 0;
					for (k = 1; k <= N; k++)
					{
						int origpos = pos;
						while ((pos < evc) && (ev[pos].first == k))
						{
							if (ev[pos].second == 'i')
							{
								//printf("%d %c => %d with %d\n",ev[pos].first,ev[pos].second,seg,goodseg);
								seg++;
							}
							pos++;
						}
						pos = origpos;
						if ((!used[k]) && ((seg-goodseg) > 0)) goodseg++;
						while ((pos < evc) && (ev[pos].first == k))
						{
							if (ev[pos].second == 'o')
							{
								//printf("%d %c => %d with %d\n",ev[pos].first,ev[pos].second,seg,goodseg);
								if (goodseg == 0)
								{
									good = 0;
									break;
								}
								goodseg--;
								seg--;
							}
							pos++;
						}
						if (good == 0) break;
					}
					if (good)
					{
						res[i] = j;
						break;
					}
					used[j] = 0;
				}
			}
		}

		//DIRTY HACKS INCOMING!
		while (1)
		{
			char kukko = 0;
			for (i = 0; i < N; i++)
			{
				for (j = 0; j < N; j++)
				{
					if (g[i][j] == 1)
					{
						if (res[i] > res[j])
						{
							kukko = 1;
							int temp = res[i];
							res[i] = res[j];
							res[j] = temp;
						}
					}
				}
			}
			if (!kukko) break;
		}


		for (i = 0; i < N; i++)
		{
			if (!((res[i] >= min[i]) && (res[i] <= max[i]))) printf("ACHTUNG!\n");
		}
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N; j++)
			{
				if (g[i][j] == 1)
				{
					if (res[i] > res[j]) printf("ACHTUNG at %d -> %d!\n",i,j);
				}
			}
		}
/*
		printf("\n");
		for (i = 0; i < N; i++) printf(" %2d",min[i]);
		printf("\n");
		for (i = 0; i < N; i++) printf(" %2d",max[i]);
		printf("\n");
		for (i = 0; i < N; i++) printf(" %2d",res[i]);
		printf("\n");
		*/

		for (i = 0; i < N; i++) printf(" %d",res[i]);
		printf("\n");

	}
	return 0;
}