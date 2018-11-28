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

const LL MOD = 1000002013;
LL	N, M, K;
pair<LL, LL>	a[1000006], b[1000006];

inline LL	calc(LL x)
{
	return x * (N + N - x + 1) / 2 % MOD;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
#endif

	LL T = read();
	for (LL t = 1; t <= T; ++ t)
	{
		N = read(), M = read(), K = 0;
		LL	ori = 0;
		for (LL i = 1; i <= M; ++ i)
		{
			LL x = read(), y = read(), z = read();
			a[++ K] = make_pair(x, - z);
			a[++ K] = make_pair(y, z);
			ori = (ori + z * calc(y - x)) % MOD;
		}
		sort(a + 1, a + K + 1);
		LL top = 0;
		LL	ans = 0;
		for (LL i = 1; i <= K; ++ i)
		{
			if (a[i].second < 0)
				b[++ top] = a[i];
			else
			{
				while (a[i].second)
				{
					if (b[top].second + a[i].second >= 0)
					{
						ans = (ans - b[top].second * calc(a[i].first - b[top].first)) % MOD;
						a[i].second += b[top].second;
						top --;
					}
					else
					{
						b[top].second += a[i].second ;
						ans = (ans + a[i].second * calc(a[i].first - b[top].first)) % MOD;
						a[i].second = 0;
					}
				}
			}
		}
		printf("Case #%I64d: %I64d\n", t, (ori - ans + MOD) % MOD);
	}
	
	return 0;
}

