#include <iostream>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
using namespace std;

const int maxn = 1000;
int n, ans, add, m;
map<string, int> p;
char ch[10000];
int curbit, has[maxn*5];

void check()
{
	int tmp = 0;
	for (int i = 1; i <= m; ++i)
		if ((has[i]&curbit) && (has[i]&~curbit))
			++tmp;
	if (ans > tmp)
		ans = tmp;
}

void dfs(int cur)
{
	if (cur == n)
	{
		check();
		return;
	}
	//printf("%02x->\n", curbit);
	curbit ^= (1<<cur);
	dfs(cur+1);
	curbit ^= (1<<cur);
	dfs(cur+1);
}

void solve()
{
	scanf("%d", &n);
	scanf("%c", &ch[0]);
	m = 0;
	p.clear();
	for (int i = 0; i < n; ++i)
	{
		int len = 0;
		while (1)
		{
			scanf("%c", &ch[len++]);
			if (ch[len-1] == '\n')
				break;
		}
		int head = 0;
		for (int j = 0; j < len; ++j)
			if (ch[j] == ' ' || ch[j] == '\n')
			{
				ch[j] = 0;
				string s(ch+head);
				int pos = p[s];
				if (pos == 0)
				{
					p[s] = pos = ++m;
					has[pos] = 0;
				}
				has[pos] |= (1<<i);
				head = j+1;
			}
	}
	curbit = 1;
	ans = ~0u>>1;
	dfs(2);
	printf("%d\n", ans);
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}