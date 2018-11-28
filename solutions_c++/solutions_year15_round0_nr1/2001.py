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

char s[1050];

void solve(int t)
{
	int n;
	scanf("%d ", &n);
	scanf("%s ", s);
	int ans = 0;
	int sum = 0;
	for (int i = 0; i <= n; ++i)
	{
		if (sum < i)
		{
			ans += i - sum;
			sum += i - sum;
		}
		sum += s[i] - '0';
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