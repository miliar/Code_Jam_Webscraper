#include<cstdio>
#define max 20000000
int cache[max];

int foo(long long n)
{
	int d = 0;
	long long t;
	if (n < max && cache[n])
	{
		d = cache[n];
	}
	else
	{
		t = n;
		while (t)
		{
			d |= 1 << (t % 10);
			t /= 10;
		}
		if (n < max) cache[n] = d;
	}
	return d;
}

long long solve(int n)
{
	int digit = foo(n);
	long long ans = n;
	while (digit ^ 0x3ff)
	{
		ans += n;
		digit |= foo(ans);
	}
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, n;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		if (!n)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		printf("Case #%d: %lld\n", t, solve(n));
	}
}