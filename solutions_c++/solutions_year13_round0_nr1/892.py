#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAXN = 5;

char str[MAXN][MAXN];
int g[MAXN][MAXN];

void init()
{
	for (int i = 1; i <= 4; ++i)
		scanf("%s", str[i] + 1);
}
int test, id;
void solve()
{
	for (int i = 1; i <= 4; ++i)
	{
		int cntX = 0, cntO = 0, flag = false;
		for (int j = 1; j <= 4; ++j)
			cntX += str[i][j] == 'X',
			cntO += str[i][j] == 'O',
			flag = (!flag) ? (str[i][j] == 'T') : true;
		if (cntX + flag == 4)
		{
			printf("Case #%d: X won\n", id);
			return ;
		}
		if (cntO + flag == 4)
		{
			printf("Case #%d: O won\n", id);
			return ;
		}
	}
	for (int i = 1; i <= 4; ++i)
	{
		int cntX = 0, cntO = 0, flag = false;
		for (int j = 1; j <= 4; ++j)
			cntX += str[j][i] == 'X',
			cntO += str[j][i] == 'O',
			flag = (!flag) ? (str[j][i] == 'T') : true;
		if (cntX + flag == 4)
		{
			printf("Case #%d: X won\n", id);
			return ;
		}
		if (cntO + flag == 4)
		{
			printf("Case #%d: O won\n", id);
			return ;
		}
	}
	int cntX = 0, cntO = 0, flag = false;
	for (int j = 1; j <= 4; ++j)
		cntX += str[j][j] == 'X',
		cntO += str[j][j] == 'O',
		flag = (!flag) ? (str[j][j] == 'T') : true;
	if (cntX + flag == 4)
	{
		printf("Case #%d: X won\n", id);
		return ;
	}
	if (cntO + flag == 4)
	{
		printf("Case #%d: O won\n", id);
		return ;
	}
	cntX = 0, cntO = 0, flag = false;
	for (int j = 1; j <= 4; ++j)
		cntX += str[j][4 - j + 1] == 'X',
		cntO += str[j][4 - j + 1] == 'O',
		flag = (!flag) ? (str[j][4 - j + 1] == 'T') : true;
	if (cntX + flag == 4)
	{
		printf("Case #%d: X won\n", id);
		return ;
	}
	if (cntO + flag == 4)
	{
		printf("Case #%d: O won\n", id);
		return ;
	}
	flag = false;
	for (int i = 1; i <= 4; ++i)
		for (int j = 1; j <= 4; ++j)
			if (str[i][j] == '.')
			{
				flag = true;
				break;
			}
	if (flag)
		printf("Case #%d: Game has not completed\n", id);
	else
	printf("Case #%d: Draw\n", id);
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
#endif
	scanf("%d", &test);
	while (test)
		++id,
		init(),
		solve(),
		--test;
	fclose(stdin);
	fclose(stdout);
	return 0;
}

