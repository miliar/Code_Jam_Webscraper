#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

int num_case, n, num[5][5], now[5][5], key[20], ans;
bool use1[5], use2[5], flag;
char s[10];

void DFS(int dep)
{
	if (dep == n + 1) return;
	bool kk;
	for (int i = 1; i <= n; i++)
		if (!use1[i])
		{
			kk = 0;
			use1[i] = 1;
			for (int j = 1; j <= n; j++)
			{
				if (!use2[j] && now[i][j])
				{
					use2[j] = 1;
					kk = 1;
					DFS(dep + 1);
					use2[j] = 0;
				}
			}
			if (!kk)
			{
				flag = 0;
				return;
			}
			use1[i] = 0;
		}
}

bool check()
{
	flag = 1;
	for (int i = 1; i <= n; i++) use1[i] = use2[i] = 0;
	DFS(1);
	return flag;
}

void calc()
{
	int tmp = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
		{
			now[i][j] = key[(i - 1) * n + j];
			if (now[i][j] < num[i][j]) return;
		}
	if (check())
	{
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				tmp += now[i][j] ^ num[i][j];
		ans = min(ans, tmp);
	}
}

void search(int dep)
{
	if (dep == n * n + 1)
	{
		calc();
		return;
	}
	key[dep] = 1;
	search(dep + 1);
	key[dep] = 0;
	search(dep + 1);
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &num_case);
	for (int icase = 1; icase <= num_case; icase++)
	{
		scanf("%d\n", &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%s", s + 1);
			for (int j = 1; j <= n; j++)
				num[i][j] = s[j] - '0';
		}
		ans = 2147483647;
		search(1);
		printf("Case #%d: %d\n", icase, ans);
	}
	return 0;
}
