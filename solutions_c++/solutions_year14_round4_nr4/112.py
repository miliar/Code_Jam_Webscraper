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

const int MOD = 1000000007;

int N, M;
int trans[100005][26], size[100005];
LL	f[105], g[105];
LL	C[105][105];

pair<int, LL>	work(int x, int N)
{
	pair<int, LL> ans = make_pair(N, 1);
	int cnt = size[x];
	for (int ch = 0; ch < 26; ++ ch)	if (trans[x][ch])
	{
		int y = trans[x][ch];
		pair<int, LL>	tmp = work(y, min(N, size[y]));
		ans.first += tmp.first;
		ans.second = ans.second * tmp.second % MOD;
		cnt -= size[y];
	}
	for (int i = 0; i <= N; ++ i)	f[i] = 0;
	f[N] = 1;
	for (int ch = 0; ch < 26; ++ ch)	if (trans[x][ch])
	{
		int y = trans[x][ch];
		int s = min(N, size[y]);
		for (int i = 0; i <= N; ++ i)	g[i] = 0;
		for (int i = 0; i <= N; ++ i)	if (f[i])
			for (int j = 0; j <= i && j <= s; ++ j)	if (s - j <= N - i)
				g[i - j] = (g[i - j] + f[i] * C[i][j] % MOD * C[N - i][s - j]) % MOD;
		//memcpy(f, g, sizeof(f));
		for (int i = 0; i <= N; ++ i)	f[i] = g[i];
	}
	LL	sum = f[0];
	if (cnt)	sum = (f[0] * N + f[1]) % MOD;
	ans.second = ans.second * sum % MOD;
	return ans;
}

char s[10005];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
#endif

	C[0][0] = 1;
	for (int i = 1; i <= 100; ++ i)
	{
		C[i][0] = 1;
		for (int j = 1; j <= 100; ++ j)
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
	}
	int __ = read();
	for (int _ = 1; _ <= __; ++ _)
	{
		printf("Case #%d: ", _);
		
		M = read();
		N = read();
		int root = 1;
		int S = 1;
		size[1] = 0;
		memset(trans[1], 0, sizeof(trans));
		for (int i = 1; i <= M; ++ i)
		{
			scanf("%s", s + 1);
			int len = strlen(s + 1);
			int x = root;
			for (int j = 1; j <= len; ++ j)
			{
				size[x] ++;
				int c = s[j] - 'A';
				if (!trans[x][c])
				{
					trans[x][c] = ++ S;
					memset(trans[S], 0, sizeof(trans[S]));
					size[S] = 0;
				}
				x = trans[x][c];
			}
			size[x] ++;
		}
		
		pair<int, LL>	ans = work(root, N);
		printf("%d %d\n", ans.first, int(ans.second));
	}


	return 0;
}

