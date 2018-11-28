#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 5000;

int st[15][N],Ans[N];
int n,m,a[3],b[3],ans;
char ch[3] = {'P', 'R', 'S'};
int Lose[3] = {1, 2, 0};

void Sort()
{
	for (int i = 0, tp = 2, half = 1; tp <= m; i ++, tp <<= 1, half <<= 1)
	{
		for (int j = 1; j <= m; j += tp)
		{
			int flag = 0;
			for (int k = j; k < j + half; k ++)
			{
				if (st[n][k] < st[n][k+half]) break;
				if (st[n][k] > st[n][k+half]) { flag = 1; break; }
			}

			if (!flag) continue;
			for (int k = j; k < j + half; k ++)
			{
				swap(st[n][k], st[n][k + half]);
			}
		}
	}

	if (ans == 1)
	{
		for (int i = 1; i <= m; i ++) Ans[i] = st[n][i];
	} else
	{
		int flag = 0;
		for (int i = 1; i <= m; i ++)
			if (Ans[i] < st[n][i]) break;
				else if (Ans[i] > st[n][i]) { flag = 1; break; }

		if (!flag) return;
		for (int i = 1; i <= m; i ++) Ans[i] = st[n][i];
	}
}

void Solve(int p)
{
	int tot = 1, tp = 0;
	st[0][1] = p;
	while (tp != n)
	{
		for (int i = 1; i <= tot; i ++)
		{
			st[tp + 1][i<<1] = st[tp][i];
			st[tp + 1][i*2-1] = Lose[st[tp][i]];
		}
		tot <<= 1, tp ++;
	}

	b[0] = b[1] = b[2] = 0;
	for (int i = 1; i <= tot; i ++) b[st[n][i]] ++;

	if (a[0] == b[0] && a[1] == b[1] && a[2] == b[2])
	{
		ans ++;
		Sort();
	}
}

int main()
{
//	freopen("data.in", "r", stdin);
//	freopen("data.out", "w", stdout);

	int CT; scanf("%d", &CT);

	for (int pt = 1; pt <= CT; pt ++)
	{
		printf("Case #%d: ", pt);

		scanf("%d", &n); m = 1 << n;
		scanf("%d%d%d", &a[1], &a[0], &a[2]);

		ans = 0;
		for (int i = 0; i < 3; i ++) Solve(i);

		if (!ans) printf("IMPOSSIBLE");
			else for (int i = 1; i <= m; i ++) printf("%c", ch[Ans[i]]);
		puts("");
	}
	return 0;
}

