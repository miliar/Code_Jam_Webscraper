#include "problemA.h"
#include <array>
#include <fstream>
#include <iostream>

using namespace std;

using Digits = std::array<bool, 10>;

Digits GetDigits(int number)
{
	Digits digits;
	digits.assign(false);

	while (number > 0)
	{
		digits[number % 10] = true;
		number /= 10;
	}

	return digits;
}

void Or(Digits& inOut, const Digits& rhs)
{
	for(auto i = 0; i < 10; i++)
	{
		inOut[i] = inOut[i] || rhs[i];
	}
}

bool AreAll(const Digits& d)
{
	for (size_t i = 0; i < 10u; i++)
	{
		if (!d[i])
			return false;
	}
	return true;
}

void problemA()
{
	ifstream fs("data/A-large.in");

	int t;

	fs >> t;

	for (auto i = 1; i <= t; i++)
	{

		int n;
		fs >> n;

		cout << "Case #" << i << ": ";
		if (n == 0)
		{
			cout << "INSOMNIA";
		}
		else
		{
			Digits named;
			named.assign(false);

			auto curr = n;

			for (;;)
			{
				Or(named, GetDigits(curr));
				if (AreAll(named))
				{
					cout << curr;
					break;
				}
				curr += n;
			}
		}
		cout << endl;
	}
}
