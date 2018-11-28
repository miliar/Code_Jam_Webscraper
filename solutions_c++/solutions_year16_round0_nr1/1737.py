#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>

using namespace std;

int bucket[10];
int n;

void cleanup()
{
	memset(bucket, 0, sizeof(bucket));
}

bool read()
{
	cleanup();
	if (scanf("%d", &n) != 1)
		return false;
	return true;
}

int update(long long n)
{
	int updated = 0;
	if (n == 0)
	{
		if (bucket[0] == 0)
			++updated;
		++bucket[0];
		return updated;
	}

	while (n > 0)
	{
		int digit = n % 10;
		n /= 10;
		if (bucket[digit] == 0)
			++updated;
		++bucket[digit];
	}

	return updated;
}

void solve()
{
	if (n == 0)
	{
		printf("INSOMNIA\n");
		return;
	}
	int i = 1;
	int still_needed = 10;
	while (still_needed > 0)
	{
		still_needed -= update(i * 1ll * n);
		++i;
	}

	printf("%lld\n", (i - 1) * 1ll * n);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int test_case = 1; test_case <= t; ++test_case)
	{
		read();
		printf("Case #%d: ", test_case);
		solve();
	}
}