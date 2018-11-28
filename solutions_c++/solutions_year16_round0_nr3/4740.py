#include <iostream>
#include <bitset>
#include <cmath>

using namespace std;

static const int MAX_N = 16;
typedef bitset<MAX_N> NumberBinaryT;
typedef unsigned long long NumberT;

int main()
{
	int T;
	cin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, J;
		cin >> N >> J;

		cout << "Case #" << nTestCase << ": " << endl;

		int numberCount = 0;
		int numberSeed = 0;
		while (numberCount < J)
		{
			// Generate a new number
			NumberBinaryT numberBinary(numberSeed);
			numberBinary <<= 1;
			numberBinary[0] = numberBinary[MAX_N - 1] = true;
			numberSeed++;

			// Verify number primality across all bases
			NumberT divisors[9] = { 0 };
			bool validNumber = true;
			for (int base = 2; base <= 10; base++)
			{
				// Compute the value according to base
				NumberT value = 0;
				for (int i = numberBinary.size() - 1; i >= 0; i--)
				{
					value *= base;
					if (numberBinary[i])
						value++;
				}

				// Find a divisor
				const NumberT divisorMax = (int)ceil(sqrt(value));
				bool foundDivisor = false;
				for (int divisor = 2; divisor < divisorMax; divisor++)
					if (value % divisor == 0)
					{
						foundDivisor = true;
						divisors[base - 2] = divisor;
						break;
					}
				if (!foundDivisor)
				{
					validNumber = false;
					break;
				}
			}
			if (validNumber)
			{
				// Valid number: print its divisors
				cout << numberBinary;
				for (int i = 0; i < sizeof(divisors) / sizeof(divisors[0]); i++)
					cout << ' ' << divisors[i];
				cout << endl;
				numberCount++;
			}
		}
	}

	return 0;
}
