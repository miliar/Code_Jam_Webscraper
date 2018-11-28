/*
* Problem: 
* Author: Leo Yu
* Time: 
* State: SOLVED
* Memo: 
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
inline int	read()
{
	int x = 0; char ch = getchar(); bool positive = 1;
	for (; ch < '0' || ch > '9'; ch = getchar())	if (ch == '-')  positive = 0;
	for (; ch >= '0' && ch <= '9'; ch = getchar())	x = x * 10 + ch - '0';
	return positive ? x : -x;
}
#define link Link
#define next Next
#define elif else if

int N, M, a[10005];
bool	use[10005];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif

	int __ = read();
	for (int _ = 1; _ <= __; ++ _)
	{
		printf("Case #%d: ", _);
		N = read(), M = read();
		for (int i = 1; i <= N; ++ i)	a[i] = read();
		sort(a + 1, a + N + 1);
		memset(use, 0, sizeof(use));
		int ans = 0;
		for (int i = 1, j = N; i <= N; ++ i)	if (!use[i])
		{
			while (j > 0 && (use[j] || a[i] + a[j] > M)) -- j;
			++ ans;
			use[i] = 1;
			if (j > 0)	use[j] = 1;
		}
		cout << ans << endl;
	}

	return 0;
}

