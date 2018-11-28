#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <limits>
#include <cmath>
#include <string>
using namespace std;
typedef unsigned long long ull;
const int N = 16;
const int J = 50;
const int primeLimit = 1000;
ull baseFactors[9][16];
ull coins[J][10];


void computeBaseFactors()
{
	for (int i = 2; i <= 10; i++)
	{
		baseFactors[i-2][0] = 1;
		for (int j = 1; j < 16; j++)
			baseFactors[i-2][j] = baseFactors[i-2][j-1] * i;
	}
}

void eratosthenesSieve(const ull &n, vector<ull> &primes)
{
	bool *sieve = new bool[n];
	memset(sieve, true, n*sizeof(bool));
	sieve[0] = false;
	sieve[1] = false;
	for (ull i = 2; i < n; i++)
	{
		if (sieve[i])
		{
			primes.push_back(i);
			for (ull j = 2 * i; j < n; j += i)
				sieve[j] = false;
		}
	}
	delete [] sieve;
}


ull convertToBase(ull n, int base)
{
	string s = std::bitset<N>(n).to_string();
	s = string(s.rbegin(), s.rend());

	ull res = 0;
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '0')
			continue;

		res += baseFactors[base-2][i];
	}
	return res;
}


int findPrimeFactor(ull n, vector<ull> &primes)
{
	for (size_t i = 0; i < primes.size(); i++)
	{
		if (n % primes[i] == 0)
			return primes[i];
	}
	return -1;
}


int main() 
{
	computeBaseFactors();
	vector<ull> primes;
	eratosthenesSieve(primeLimit, primes);

	ull current = 1 << (N-1);
	current++;

	int foundCoins = 0;
	while (foundCoins < J)
	{
		coins[foundCoins][0] = convertToBase(current, 10);
		for (int b = 2; b <= 10; b++)
		{
			ull k = convertToBase(current, b);
			int p = findPrimeFactor(k, primes);
			if (p == -1)
				break;
			coins[foundCoins][b-1] = p;
			if (b == 10)
				foundCoins++;
		}
		current += 2;
	}

	cout << "Case #1:" << endl;
	for (int i = 0; i < J; i++)
	{
		for (int j = 0; j < 10; j++)
			cout << coins[i][j] << " ";
		cout << endl;
	}
	return 0;
}


