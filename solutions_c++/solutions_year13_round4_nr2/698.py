#include <stdio.h>

long long gWin(int n, long long p)
{
	long long ans = 0ll;
	long long tmp = 2ll;
	bool has = true;
	p -= 1;
	for (int i=n-1;i>0;--i)
	{
		has = has&&((1ll<<i)&p);
		if (has)
			ans |= tmp;
		tmp <<= 1;
	}
	if (has&&(p%2))
		++ans;
	return ans;
}

long long cWin(int n, long long p)
{
	long long ans = 0ll;
	long long tmp = 1ll;
	bool has = false;
	p >>= 1;
	for (int i=n-1;i>=0;--i)
	{
		if (!has)
			has = (1ll<<i)&p;
		if (has)
			ans |= tmp;
		tmp <<= 1;
	}
	return ans;
}

int main()
{
	int t;
	int n;
	long long p;
	scanf("%d", &t);
	for (int i=1;i<=t;++i)
	{
		scanf("%d%lld", &n, &p);
		printf("Case #%d: %lld %lld\n", i, gWin(n, p), cWin(n, p));
	}
	return 0;
}
