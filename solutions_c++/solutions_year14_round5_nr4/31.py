#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 85
#define MYINF 1000000000

using namespace std;

static char b[MAXN][MAXN];
static int C[MAXN];

int N;

int DFS (int point, int par)
{
	int i;
	int max = 0;
	for (i = 0; i < N; i++)
	{
		if ((b[point][i]) && (i != par))
		{
			int temp = DFS(i,point);
			if (temp > max) max = temp;
		}
	}
	return max + C[point];
}

char CanReach (int point, int par, int what)
{
	if (point == what) return 1;
	int i;
	for (i = 0; i < N; i++)
	{
		if ((b[point][i]) && (i != par))
		{
			if (DFS(i,point)) return 1;
		}
	}
	return 0;
}

int GetA (int x, int y)
{
	if (x == y)
	{
		int res = -MYINF;
		int z;
		for (z = 0; z < N; z++)
		{
			if (b[x][z])
			{
				b[x][z] = 0;
				b[z][x] = 0;
				int tempC = C[x];
				C[x] = 0;
				int pA = DFS(z,-1) + tempC;
				int pB = DFS(x,-1);
				C[x] = tempC;
				b[x][z] = 1;
				b[z][x] = 1;
				if ((pA - pB) > res) res = pA - pB;
			}
		}
		if (res == -MYINF)
		{
			int tempC = C[x];
			C[x] = 0;
			int pA = tempC;
			int pB = DFS(x,-1);
			C[x] = tempC;
			if ((pA - pB) > res) res = pA - pB;
		}
		return res;
	}
	else
	{
		int res = -MYINF;
		int z;
		for (z = 0; z < N; z++)
		{
			if (b[x][z])
			{
				if (CanReach(z, x, y))
				{
					b[x][z] = 0;
					b[z][x] = 0;
					int tempC = C[x];
					C[x] = 0;
					int temp = tempC - GetA(y, z);
					C[x] = tempC;
					b[x][z] = 1;
					b[z][x] = 1;
					if (temp > res) res = temp;
				}
				else
				{
					b[x][z] = 0;
					b[z][x] = 0;
					int tempC = C[x];
					C[x] = 0;
					int pA = DFS(z,-1) + tempC;
					int pB = DFS(y,-1);
					C[x] = tempC;
					b[x][z] = 1;
					b[z][x] = 1;
					if ((pA - pB) > res) res = pA - pB;
				}
			}
		}
		if (res == -MYINF)
		{
			int tempC = C[x];
			C[x] = 0;
			int pA = tempC;
			int pB = DFS(y,-1);
			C[x] = tempC;
			if ((pA - pB) > res) res = pA - pB;
		}
		return res;
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		scanf("%d",&N);
		int i, j;
		for (i = 0; i < N; i++)
		{
			scanf("%d",&(C[i]));
		}
		memset(b,0,sizeof(b));
		for (i = 0; i < (N-1); i++)
		{
			scanf("%d",&j);
			j--;
			b[i][j] = 1;
			b[j][i] = 1;
		}
		int res = -MYINF;
		int root;
		for (root = 0; root < N; root++)
		{
			int min = MYINF;
			for (j = 0; j < N; j++)
			{
				int now = GetA(root, j);
				//printf("%d,%d = %d\n",root,j,now);
				if (now < min) min = now;
			}
			if (min > res) res = min;
		}
		printf("Case #%d: %d\n",iT+1,res);
	}
	return 0;
}
