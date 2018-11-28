#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool isPrime(unsigned long long nb, unsigned long long& divisor)
{
	if (nb % 2 == 0)
	{
		divisor = 2;
		return false;
	}

	for (unsigned long long n = 3; n < std::sqrt(nb); n += 2)
	{
		if (nb % n == 0)
		{
			divisor = n;
			return false;
		}
	}

	return true;
}

unsigned long long pow(int nb, int exp)
{
	if (exp == 0)
		return 1;

	unsigned long long res = nb;
	for (int i = 1; i < exp; ++i)
	{
		res *= nb;
	}

	return res;
}

void increaseCoin(std::vector<bool>& coin)
{
	for (std::vector<bool>::iterator it = coin.begin() + 1; it != coin.end() - 1; ++it)
	{
		it.operator*().flip();

		if (*it)
			return;
	}
}

unsigned long long numberInBase(const std::vector<bool>& coin, int base)
{
	unsigned long long res = 0;
	for (int i = 0; i < coin.size(); ++i)
	{
		if (coin[i])
		{
			res += pow(base, i);
		}
	}

	return res;
}

std::string WriteOut(const vector<bool>& data)
{
	std::string stream;

	for (vector<bool>::const_iterator it = data.begin(); it != data.end(); it++) {
		stream += std::to_string(*it);
	}

	reverse(stream.begin(), stream.end());

	return stream;
}

int main()
{
	ifstream inputFile("test.txt");
	ofstream outputFile("output.txt");

	int testNumber = 0;

	inputFile >> testNumber;

	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": " << endl;
		int coinNumbers;
		int size;

		inputFile >> size;
		inputFile >> coinNumbers;

		std::vector<bool> coin(size, false);
		*coin.begin() = true;
		*(coin.end() - 1) = true;
		int solved = 0;
		std::vector<long long> divisors;
		std::vector<string> results;

		while (results.size() < coinNumbers)
		{
			for (int i = 2; i <= 10; ++i)
			{
				unsigned long long nb = numberInBase(coin, i);
				unsigned long long divisor;
				if (isPrime(nb, divisor))
				{
					divisors.clear();
					break;
				}
				divisors.push_back(divisor);
			}

			if (divisors.size() == 9)
			{
				std::string res = WriteOut(coin);
				if (std::find(results.begin(), results.end(), res) == results.end())
				{
					results.push_back(res);

					outputFile << res << " ";
					int cpt = 2;
					for (unsigned long long nb : divisors)
					{
						outputFile << nb << " ";
						++cpt;
					}
					outputFile << endl;
				}

				divisors.clear();
			}

			increaseCoin(coin);
		}
	}

	return 0;
}
