#include <fstream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

long long ConvertFrom(string, int);
int IsPrime(long long);

int main()
{
	int numberOfCases;
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	in >> numberOfCases;
	for (int i = 0; i < numberOfCases; i++)
	{
		out << "Case #" << i + 1 << ":" << endl;
		int length, numberOfCoins;
		string coinBase = "";
		in >> length >> numberOfCoins;
		int coinsFound = 0;
		for (int j = 0; j < length - 2; j++)
		{
			if (j < ((length - 2) / 2) + 1)
				coinBase += '0';
			else
				coinBase += '1';
		}
		do
		{
			string coin = "1" + coinBase + "1";
			map<int, long long> divisors;
			bool prime = false;
			for (int j = 2; j < 11; j++)
			{
				long long temp;
				temp = ConvertFrom(coin, j);
				long long divisor = IsPrime(temp);
				if (divisor == 0)
				{
					prime = true;
					break;
				}
				divisors[j] = divisor;
			}
			if (prime)
				continue;
			out << coin;
			for (int j = 2; j < 11; j++)
			{
				out << " " << divisors[j];
			}
			out << endl;
			coinsFound++;
		} while (next_permutation(coinBase.begin(), coinBase.end()) && coinsFound < numberOfCoins);
	}
	return 0;
}

long long ConvertFrom(string number, int base)
{
	long long result = 0;
	for (int i = 0; i < number.length(); i++)
	{
		if (number[i] == '1')
			result += pow(base, number.length() - i - 1);
	}
	return result;
}

int IsPrime(long long p)
{
	int primes[100] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
		101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
		239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
		397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541 };
	for (int i = 0; i < 100; i++)
	{
		if (sqrt(p) + 1 <= primes[i])
		{
			return 0;
		}
		if (p % primes[i] == 0)
		{
			if (p == primes[i])
				return 0;
			return primes[i];
		}
	}
	for (int div = 543; div < sqrt(p) + 1; div += 2)
	{
		if (p % div == 0)
		{
			return div;
		}
	}
	return 0;
}