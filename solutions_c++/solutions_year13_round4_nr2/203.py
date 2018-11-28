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
inline LL	read()
{
	LL x = 0; char ch = getchar(); bool positive = 1;
	for (; ch < '0' || ch > '9'; ch = getchar())	if (ch == '-')  positive = 0;
	for (; ch >= '0' && ch <= '9'; ch = getchar())	x = x * 10 + ch - '0';
	return positive ? x : -x;
}
#define link Link

LL	N, P, M;

inline bool	check(LL x)
{
	for (LL l = 1, r = M, b = x - 1; ; )
	{
		LL	mid = l + r >> 1;
		if (P <= mid)	return b == 0;
		if (b == 0)	return 0;
		b --;
		b /= 2;
		l = mid + 1;
	}
	return 1;
}

inline bool check2(LL x)
{
	for (LL l = 1, r = M, s = M - x; ; )
	{
		LL	mid = l + r >> 1;
		if (P > mid)	return s > 0 || P == r;
		if (s == 0)	return 0;
		s --;
		s /= 2;
		r = mid;
	}
	return 1;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#endif

	int T = read();
	for (int t = 1; t <= T; ++ t)
	{
		printf("Case #%d: ", t);
		N = read(), P = read(), M = 1ll << N;
		if (P == M)
		{
			printf("%I64d %I64d\n", M - 1, M - 1);
			continue;
		}
		LL l = 1, r = M;
		while (l + 1 < r)
		{
			LL	mid = l + r >> 1;
			if (check(mid))	l = mid;
			else	r = mid;
		}
		printf("%I64d ", l - 1);
		l = 1, r = M;
		while (l + 1 < r)
		{
			LL	mid = l + r >> 1;
			if (check2(mid))	l = mid;
			else	r = mid;
		}
		printf("%I64d\n", l - 1);
	}

	return 0;
}

