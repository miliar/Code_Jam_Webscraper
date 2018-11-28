#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

long long IntegerPower(long long base, long long power)
{
	long long result = 1;
	for (long long i = 0; i < power; i++)
		result *= base;
	return result;
}

long long CalculateModulusPower(long long base, long long exponent, long long modulus)
{
	long long result = 1;
	for (long long i = 0; i < exponent; i++)
	{
		result *= base;
		result = result % modulus;
	}
	return result;
}

bool ProperDivisorExists(const vector<long long>& coin, long long base, long long& result)
{
	const long long timeout = 1;
	auto coinSize = static_cast<int>(coin.size());
	auto upperLimit = IntegerPower(base, coinSize / 2);
	long long reducedSum;
	auto startTime = high_resolution_clock::now();
	for (long long divisor = 2; divisor <= upperLimit; divisor++)
	{
		reducedSum = 0;
		for (int i = 0; i < coinSize; i++)
			if (coin[i] != 0)
				reducedSum += CalculateModulusPower(base, i, divisor);
		if (reducedSum % divisor == 0)
		{
			result = divisor;
			return true;
		}
		if (duration_cast<milliseconds>(high_resolution_clock::now() - startTime).count() > timeout)
			break;
	}
	return false;
}

void SetBinaryArray(vector<long long>& coin, long long number)
{
	auto exponentSize = static_cast<long long>(coin.size());
	for (long long i = 0; i < exponentSize; i++)
		coin[i] = (number & IntegerPower(2, i)) >> i;
}

pair<long long, long long> GetLengthAndCount()
{
	int length, count;
	cin >> length >> count;
	return make_pair(length, count);
}

void PrintResult(const vector<long long>& coin, const vector<long long>& divisors)
{
	for (long long i = coin.size() - 1; i >= 0; i--)
		cout << coin[i];
	for (auto value : divisors)
		cout << " " << value;
	cout << "\n";
}

//We could even parallelize the main loop but this isn't necessary for this problem
int main()
{
	int testCases;
	cin >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		printf("Case #%i:\n", i);
		auto lengthAndCount = GetLengthAndCount();
		vector<long long> coin(lengthAndCount.first, 0);
		auto limit = IntegerPower(2, lengthAndCount.first);
		long long counter = 0;
		auto upperOne = limit / 2;
		for (auto binaryNumber = upperOne + 1; binaryNumber < limit; binaryNumber += 2)
		{
			SetBinaryArray(coin, binaryNumber);
			auto divisorExists = true;
			vector<long long> divisors;
			for (long long j = 2; j <= 10; j++)
			{
				long long divisor;
				divisorExists = divisorExists && ProperDivisorExists(coin, j, divisor);
				if (!divisorExists)
					break;
				divisors.push_back(divisor);
			}
			if (divisorExists)
			{
				counter++;
				PrintResult(coin, divisors);
			}

			if (counter >= lengthAndCount.second)
				break;
		}
	}

	return 0;
}

