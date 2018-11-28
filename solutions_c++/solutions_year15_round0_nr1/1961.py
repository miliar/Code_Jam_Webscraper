// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <map>
#include <list>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int n;
char s[10000];

int solve()
{
	int ans = 0;
	int sum = 0;
	for (int i = 0; i <= n; i++)
	{
		if (s[i] == '0') continue;
		if (ans + sum < i)
		{
			ans += i - sum - ans;
		}
		sum += s[i] - '0';
	}
	return ans;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d %s", &n, s);
		printf("Case #%d: %d\n", t, solve());
	}
	return 0;
}

