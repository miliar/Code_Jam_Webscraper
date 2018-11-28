/************************************************************************/
/* Microsoft Visual Studio Community 2013, Win32                        */
/************************************************************************/

#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

typedef unsigned long long SIZE;

SIZE number_in_base(SIZE x, SIZE b, SIZE n)
{
	SIZE result = 1;
	SIZE bb = b;
	for (SIZE i = 0; i < n - 2; ++i, bb*=b)
	{
		result += ((1llu << i) & x) ? bb : 0;
	}
	result += bb;
	return result;
}

/************************************************************************/
/* finds smallest non-trivial possible divisor. For primes it returns 1 */
/* see https://en.wikipedia.org/wiki/Primality_test#Pseudocode          */
/************************************************************************/
SIZE find_divisor(SIZE n)
{
	if (n <= 3)
		return 1;
	if (n % 2 == 0)
		return 2;
	if (n % 3 == 0)
		return 3;
	SIZE i = 5;
	while (i*i <= n)
	{
		if (n % i == 0)
			return i;
		i += 2;
		if (n % i == 0)
			return i;
		i += 4;
	}
	return 1;
}

int main(int argc, char* argv[])
{
	SIZE cases, j,n;
	cin >> cases;
	for (SIZE i = 1; i <= cases; ++i)
	{
		cin >> n >> j;

		printf("Case #%llu:\n", i);
		SIZE already_found = 0;
		for (SIZE number_binary = 0; number_binary < pow(2llu, n-2); ++number_binary)
		{
			vector<SIZE> divisors;
			SIZE x;
			for (SIZE b = 2; b <= 10; ++b)
			{
				x = number_in_base(number_binary, b, n);
				auto const d = find_divisor(x);
				if (d > 1)
					divisors.push_back(d);
				else
					break;
			}
			if (divisors.size() == 9)
			{
				printf("%llu", x);
				for (SIZE d : divisors)
					printf(" %lld", d);
				printf("\n");
				++already_found;
			}
			if (already_found >= j)
				return 0;
		}
	}

	return 0;
}

