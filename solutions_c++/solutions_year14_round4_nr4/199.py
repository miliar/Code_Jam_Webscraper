#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <algorithm>
#define MAXN 15
#define MOD 1000000007

using namespace std;

int res;
int cnt;
static char data[MAXN][MAXN];
static int w[MAXN];
int N, S;

void DFS (int point)
{
	if (point == N)
	{
		int now = 0;
		int s, i, j, k;
		for (s = 0; s < S; s++)
		{
			i = 0;
			while ((i < N) && (w[i] != s)) i++;
			if (i == N) return;
		}
		for (s = 0; s < S; s++)
		{
			now++;
			for (i = 0; i < N; i++)
			{
				if (w[i] == s)
				{
					for (k = 1; k <= (int)strlen(data[i]); k++)
					{
						char flag = 0;
						for (j = 0; j < i; j++)
						{
							if (w[j] == s)
							{
								if (!strncmp(data[i], data[j], k))
								{
									flag = 1;
									break;
								}
							}
						}
						if (!flag) now++;
					}
				}
			}
		}
		if (now > res)
		{
			res = now;
			cnt = 1;
		}
		else if (now == res)
		{
			cnt = (cnt + 1) % MOD;
		}
	}
	else
	{
		int i;
		for (i = 0; i < S; i++)
		{
			w[point] = i;
			DFS(point+1);
		}
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		scanf("%d %d",&N,&S);
		int i;
		for (i = 0; i < N; i++) scanf("\n%s",data[i]);
		res = 0;
		cnt = 1;
		DFS(0);
		printf("Case #%d: %d %d\n",iT+1,res,cnt);
	}
	return 0;
}
