#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 1 << 13;
int cnt[3], n, len;
int que[N], ans[N];

void init()
{
	scanf("%d", &n);
	len = 1 << n;
	for (int i = 0; i < 3; ++ i) scanf("%d", &cnt[i]);
	swap(cnt[0], cnt[1]);
}

void dfs(int l, int r, int tp)
{
	if (l == r)
	{
		que[l] = tp;
		return;
	}
	int Ano = (tp + 2) % 3;
	int mid = (l + r) >> 1;
	dfs(l, mid, tp), dfs(mid + 1, r, Ano);
	int Flag = 0;
	for (int i = l, j = mid + 1; i <= mid; ++ i, ++ j) if (que[i] < que[j]) 
	{
		Flag = 0;
		break;
	}
	else if (que[i] > que[j]) 
	{
		Flag = 1;
		break;
	}
	if (Flag)
	{
		for (int i = l, j = mid + 1; i <= mid; ++ i, ++ j)
			swap(que[i], que[j]);
	}
}

int main()
{
	//freopen("1.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	int T, Case = 0;
	scanf("%d", &T);
	while (T --)
	{	
		init();
		int Flag = 0;
		for (int win = 0; win < 3; ++ win)
		{
			dfs(1, len, win);
			int cur[3];
			memset(cur, 0, sizeof(cur));
			for (int i = 1; i <= len; ++ i) ++ cur[que[i]];
			int flag = 1;
			for (int i = 0; i < 3 && flag; ++ i) flag = cur[i] == cnt[i];
			if (!flag) continue;
			if (!Flag)
			{
				Flag = 1;
				memcpy(ans, que, sizeof(ans));
			}
			else 
			{
				Flag = 0;
				for (int i = 1; i <= len; ++ i) if (ans[i] < que[i]) 
				{
					Flag = 0;
					break;
				}
				else if (ans[i] > que[i])
				{
					Flag = 1;
					break;
				}
				if (Flag)
					memcpy(ans, que, sizeof(ans));
				Flag = 1;
			}
		}
		printf("Case #%d: ", ++ Case);
		if (!Flag)
			puts("IMPOSSIBLE");
		else 
		{
			for (int i = 1; i <= len; ++ i) if (ans[i] == 0) printf("P");
			else if (ans[i] == 1) printf("R");
			else printf("S");
			puts("");
		}
	}
}