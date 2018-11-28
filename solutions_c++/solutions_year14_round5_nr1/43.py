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

LL	N, p, q, r, s, a[1000006];

inline bool	check(LL limit)
{
	LL	now = limit, cnt = 1;
	for (int i = 0; i < N; ++ i)
	{
		if (now < a[i])
		{
			cnt ++;
			now = limit;
			if (cnt > 3)	return 0;
		}
		now -= a[i];
	}
	return 1;
}

inline void	Main()
{
	N = read(), p = read(), q = read(), r = read(), s = read();
	LL	L = 0, S = 0;
	for (int i = 0; i < N; ++ i)
	{
		a[i] = (LL(i) * LL(p) + LL(q)) % r + s;
		S += a[i];
		L = max(L, a[i] - 1);
	}
	LL	R = S;
	while (L + 1 < R)
	{
		LL m = L + R >> 1;
		if (check(m))	R = m;
		else	L = m;
	}
	printf("%.15lf\n", double(S - R) / double(S));
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif

	int T = read();
	for (int t = 1; t <= T; ++ t)
	{
		printf("Case #%d: ", t);
		Main();
	}

	return 0;
}

