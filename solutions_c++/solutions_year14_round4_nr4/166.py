#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <string>
#define PQ priority_queue
#define OO 2147483647
#define Max(a, b) ((FASTBUFFER = ((a) - (b)) >> 31), ((b) & FASTBUFFER | (a) & ~FASTBUFFER))
#define Min(a, b) ((FASTBUFFER = ((a) - (b)) >> 31), ((a) & FASTBUFFER | (b) & ~FASTBUFFER))
#define Swap(a, b) (a ^= b, b ^= a, a ^= b)

int FASTBUFFER;

using namespace std;

vector <int> v[105];
int test, tt, n, m, i, ans1, ans2, tot;
int next[1005][1005];
char str[105][105];

void dfs(int i);
void init();
void add(char str[]);

int main()
{
	freopen("D-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		scanf("%d %d", &n, &m);
		for (i = 1; i <= n; i++)
			scanf("%s", str[i] + 1);
		ans1 = 0, ans2 = 0;
		dfs(1);
		printf("Case #%d: %d %d\n", ++tt, ans1, ans2);
	}
	
	return 0;
}

void dfs(int i)
{
	if (i > n)
	{
		int s = 0;
		for (int x = 1; x <= m; x++)
			if (v[x].empty())
				return;
		for (int x = 1; x <= m; x++)
		{
			init();
			for (int j = 0; j < v[x].size(); j++)
				add(str[v[x][j]]);
			s += tot + 1;
		}
		
		if (s > ans1)
			ans1 = s, ans2 = 0;
		if (s == ans1)
			ans2++;
		return;
	}
	
	for (int x = 1; x <= m; x++)
	{
		v[x].push_back(i);
		dfs(i + 1);
		v[x].pop_back();
	}
}

void init()
{
	for (int i = 0; i <= tot; i++)
		for (char c = 'A'; c <= 'Z'; c++)
			next[i][c] = 0;
	tot = 0;
}

void add(char str[])
{
	int now = 0;
	for (int i = 1; str[i]; i++)
	{
		if (next[now][str[i]] == 0)
			next[now][str[i]] = ++tot;
		now = next[now][str[i]];	
	}
}
