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

int P, Q, N, M, H[105], G[105];
int f[105][205][1005];

inline void	Main()
{
	P = read(), Q = read(), N = read();
	int S = 0;
	for (int i = 1; i <= N; ++ i)
	{
		H[i] = read();
		S += (H[i] + Q - 1) / Q;
		G[i] = read();
	}
	memset(f, 188, sizeof(f));
	f[1][0][1] = 0;
	int ans = 0;
	for (int i = 1; i <= N; ++ i)
	for (int j = 0; j < H[i]; ++ j)
	for (int k = 0; k <= S; ++ k)	if (f[i][j][k] >= 0)
	{
		if (k)
		{
			if (j + P >= H[i])
				f[i + 1][0][k - 1] = max(f[i + 1][0][k - 1], f[i][j][k] + G[i]);
			else
				f[i][j + P][k - 1] = max(f[i][j + P][k - 1], f[i][j][k]);
		}
		if (j + Q >= H[i])
			f[i + 1][0][k + 1] = max(f[i + 1][0][k + 1], f[i][j][k]);
		else
			f[i][j + Q][k + 1] = max(f[i][j + Q][k + 1], f[i][j][k]);
	}
	for (int i = 0; i <= S; ++ i)
		ans = max(ans, f[N + 1][0][i]);
	cout << ans << endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif

	int T = read();	
	for (int t = 1; t <= T; ++ t)
	{
		printf("Case #%d: ", t);
		Main();
	}

	return 0;
}

