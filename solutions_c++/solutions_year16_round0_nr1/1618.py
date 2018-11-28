#include <iostream>


using namespace std;

typedef long long LL;

const int DIGITS = 10;

int update_digits(LL n, bool digitSeen[])
{
	int d;
	int count = 0;
	while (n > 0)
	{
		d = n % DIGITS;
		n /= DIGITS;
		count += !digitSeen[d];
		digitSeen[d] = true;
	}
	return count;
}

LL solve(LL n)
{
	int k;
	int count = 0;
	bool digitSeen[DIGITS] = {};
	for (k = 1; count < DIGITS && k <= 10000000; k++)
	{
		count += update_digits(k * n, digitSeen);
	}
	if (count == DIGITS)
		return (k - 1) * n;
	else
		return -1;
}

int main()
{
	/*
	for (int k = 1; k <= 1000000; k++)
		if (solve(k) == -1)
			printf("Failure: N = %d\n", k);
	*/

	int cases;
	LL n;
	cin >> cases;
	for (int c = 1; c <= cases; c++)
	{
		cin >> n;
		if (n > 0)
			printf("Case #%d: %lld\n", c, solve(n));
		else
			printf("Case #%d: INSOMNIA\n", c);
	}
	return 0;
}