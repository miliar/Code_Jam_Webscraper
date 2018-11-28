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

void solve(int t)
{
	int n;
	long long p, q;
	scanf("%d%lld", &n, &p);
	--p;
	long long P = p;
	if (P == (1LL << n) - 1)
	{
		printf("Case #%d: %lld %lld\n", t + 1, (1LL << n) - 1, (1LL << n) - 1);
		return;
	}
	int i;
	q = 0;
	for (i = 0; i < n; ++i)
	{
		q = (q*2 + (p%2));
		p = p/2;
	}
	long long ans1 = 2;
//	printf("%lld %lld\n", P, q);
	while (q%2 == 1)
	{
		q /= 2;
		ans1 *= 2;
	}
	long long ans2 = 0;
	i = 0;
//	printf("%lld\n", P);
	while (ans2 + (1LL << i) <= P)
	{
		ans2 += (1LL << i);
		++i;
	}
	long long ans3 = 0;
	for (i = 0; i < n; ++i)
	{
		ans3 = ans3*2 + (ans2%2);
		ans2 /= 2;
//		printf("%lld\n", ans3);
	}
	printf("Case #%d: %lld %lld\n", t + 1, ans1 - 2, ans3);
//	exit(0);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int i, T;
	scanf("%d", &T);
	for (i = 0; i < T; ++i)
		solve(i);
	return 0;
}