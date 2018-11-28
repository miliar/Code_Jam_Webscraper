#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
using namespace std;

string to_binary(unsigned x)
{
	string result;
	while (x)
	{
		result.push_back((x & 1) + '0');
		x >>= 1;
	}
	reverse(result.begin(), result.end());
	return result;
}

void generatePrimes(vector < int > &primes, const int N)
{
	vector<bool> prime(N + 1, true);
	prime[0] = prime[1] = false;
	for (int i = 2; i <= N; ++i)
		if (prime[i])
		{
			primes.push_back(i);
			if (i * 1ll * i <= N)
				for (int j = i*i; j <= N; j += i)
					prime[j] = false;

		}
}

map < string, list < int > > jemicoins;
void precalculateSmall()
{
	const int N = 16;
	const int J = 50;
	
	vector < int > primes;
	generatePrimes(primes, (int)1e9);


	for (unsigned mask = 0; mask <= (1 << N) && jemicoins.size() < J; ++mask)
	{
		if ((mask >> (N - 1)) == 1 && (mask & 1) == 1)
		{
			string binary = to_binary(mask);
			list < int > dividers;
			for (int base = 2; base <= 10; ++base)
			{
				long long number = stoll(binary.c_str(), NULL, base);
				int found = 0;
				for (int prime : primes)
				{
					if (number % prime == 0)
					{
						found = prime;
						break;
					}
					else if (1LL * prime * prime > number)
					{
						break;
					}
				}
				if (found)
				{
					dividers.push_back(found);
				}
				else
				{
					break;
				}
			}
			if (dividers.size() == 9)
			{
				jemicoins.insert(make_pair(binary, dividers));
			}
			assert(dividers.size() <= 9);
		}
	}
}

void printSmall()
{
	for (auto jemicoin : jemicoins)
	{
		printf("%s ", jemicoin.first.c_str());
		for (int divider : jemicoin.second)
		{
			printf("%d ", divider);
		}
		putchar('\n');
	}
}

int main()
{
	precalculateSmall();
	int t;
	scanf("%d", &t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int n, j;
		scanf("%d%d", &n, &j);
		printf("Case #%d:\n", testcase);
		printSmall();
	}

	return 0;
}
