#include <iostream>
#include <cstdio>
using namespace std;

int n, p;

bool check1(long long x)
{
	long long now = 1LL << n;
	long long nowr = 0;
	for (int i = 1; i <= n; i++)
	{
		now >>= 1;
		if (x > 1)
		{
			x /= 2;
			nowr += now;
		}
		else break;
	}
	return nowr < p;
}

bool check2(long long x)
{
	long long now = 1LL << n;
	long long nowr = 0;
	for (int i = 1; i <= n; i++)
	{
		now >>= 1;
		if (x < (now << 1))
		{
			x -= (x - 1) / 2;
		}
		else nowr += now;
	}
	return nowr < p;
}

long long searchans1()
{
	long long left = 1, right = 1LL << n, mid;
	if (p == right) return right - 1;
	while (left + 1 < right)
	{
		mid = (left + right) / 2;
		if (check1(mid)) left = mid; else right = mid;
	}
	return left - 1;
}

long long searchans2()
{
	long long left = 1, right = 1LL << n, mid;
	if (p == right) return right - 1;
	while (left + 1 < right)
	{
		mid = (left + right) / 2;
		if (check2(mid)) left = mid; else right = mid;
	}
	return left - 1;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%lld", &n, &p);
		printf("Case #%d: %lld %lld\n", i, searchans1(), searchans2());
	}
	return 0;
}
