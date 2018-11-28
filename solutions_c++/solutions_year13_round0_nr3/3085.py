#include <iostream>
#include <cstdio>
using namespace std;

int reverse(int x)
{
	int ans = 0;
	while (x)
	{
		ans = ans * 10 + x % 10;
		x /= 10;
	}
	return ans;
}

bool checkpalin(long long x)
{
	return x == reverse(x);
}

int counting(long long x)
{
	int ans = 0;
	
	int now = 1;
	for (int i = 1; i <= 10000; i++)
	{
		if (i / now) now *= 10;
		long long k = i * now + reverse(i);
		k *= k;
		if (k > x) break;
		if (checkpalin(k)) ans++;
	}
	
	now = 1;
	for (int i = 1; i <= 20000; i++)
	{
		if (i / now) now *= 10;
		long long k = (i - i % 10) * (now / 10) + reverse(i);
		k *= k;
		if (k > x) break;
		if (checkpalin(k)) ans++;
	}
	
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		long long x, y;
		scanf("%lld%lld", &x, &y);
		printf("Case #%d: %d\n", i, counting(y) - counting(x - 1));
	}
	return 0;
}
