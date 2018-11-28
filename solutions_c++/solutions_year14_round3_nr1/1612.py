#include <cstdio>
#include <algorithm>
#include <set>
#include <cmath>
#include <iostream>

using namespace std;

unsigned long gcd(unsigned long num1, unsigned long num2)
{
	unsigned long temp;

	while (num2 != 0)
	{
		temp = num2;
		num2 = num1 % num2;
		num1 = temp;
	}

	return num1;
}

int main(void)
{
	unsigned int test_count;
	scanf("%u\n", &test_count);

	unsigned long compare_bits[40];
	for (unsigned int index = 0; index < 40; ++index)
	{
		compare_bits[index] = 1 << index;
	}

	for (unsigned int test = 0; test < test_count; ++test)
	{
		printf("Case #%u: ", test + 1);

		unsigned long numer;
		unsigned long denom;
		scanf("%lu/%lu\n", &numer, &denom);

		unsigned long divisor = gcd(numer, denom);

		numer /= divisor;
		denom /= divisor;

		int couldBeElf = 0;
		for (unsigned int index = 0; index < 40; ++index)
		{
			if (compare_bits[index] == denom)
			{
				couldBeElf = 1;
			}
		}

		if (!couldBeElf)
		{
			cout << "impossible" << endl;
			continue;
		}

		//cout << numer << endl;
		//cout << denom << endl;

		couldBeElf = 0;
		unsigned int generation = 0;
		while (generation < 40)
		{
			if (numer >= denom)
			{
				numer /= 2;
				break;
			}
			else
			{
				numer *= 2;
				++generation;
			}
		}

		cout << generation << endl;
	}
}
