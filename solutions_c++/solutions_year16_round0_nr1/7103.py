#include <cstdio>
#include <cassert>
#include <set>
using namespace std;

long long solveSmall(long long n)
{
	assert(n);
	set < int > digits;
	long long current = n;
	while (digits.size() < 10)
	{
		for (long long x = current; x; x /= 10)
		{
			digits.insert(x % 10);
		}
		current += n;
	}
	assert(digits.size() == 10);
	return current - n;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int n;
		scanf("%d", &n);
		if (n)
		{
			printf("Case #%d: %I64d\n", testcase, solveSmall(n));
		}
		else
		{
			printf("Case #%d: INSOMNIA\n", testcase);
		}
	}
	return 0;
}
