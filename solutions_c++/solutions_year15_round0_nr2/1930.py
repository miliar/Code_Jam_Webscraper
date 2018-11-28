#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

const int MAXP = 1000;

int p[1050];

void solve(int t)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &p[i]);
	}
	int ans = MAXP;
	for (int i = 1; i <= MAXP; ++i)
	{
		int spec = 0;
		for (int j = 0; j < n; ++j)
		{
			spec += (p[j] + i - 1)/i - 1;
		}
		if (spec + i < ans)
		{
			ans = spec + i;
		}
	}
	printf("Case #%d: %d\n", t, ans);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		solve(i + 1);
	}
	return 0;
}
