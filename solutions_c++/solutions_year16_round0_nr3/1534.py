#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <random>
#include <ctime>
#include <unordered_set>
#include <vector>
#include <map>

using namespace std;

std::unordered_set< std::string > checked;
int n, needed;
int printed;

long long divisor(long long n)
{
	if (n == 1)
		return 1;
	if (n == 2)
		return 2;
	if (n % 2 == 0)
		return 2;
	for (long long i = 3; i * i <= n; i+=2)
		if (n % i == 0)
			return i;
	return n;
}

long long interpretInBase(const std::string& num, int base)
{
	long long res = 0;
	for (int i = 0; i < num.size(); ++i)
	{
		res *= base;
		res += (num[i] - '0');
	}
	return res;
}

std::map< std::vector <long long>, std::vector <string> > m;

void check(string& s)
{
	vector <long long> divisors;
	for (int i = 2; i <= 10; ++i)
	{
		long long temp = interpretInBase(s, i);
		long long div = divisor(temp);
		if (div == temp)
			return;
		divisors.push_back(div);
	}
	m[divisors].push_back(s);
	printed += m[divisors].size();
}

void cleanup()
{
	checked.clear();
	printed = 0;
}

void read()
{
	scanf("%d%d", &n, &needed);
}

const int max_length = 16;

void generate()
{
	for (int length = max_length; length <= max_length; ++length)
	{
		for (int mask = 3; mask < (1 << length); ++mask)
		{
			if ((mask & 1) && mask & (1 << (length - 1)))
			{
				std::string s;
				for (int i = 0; i < length; ++i)
				{
					if (mask & (1 << i))
						s.push_back('1');
					else
						s.push_back('0');
				}
				check(s);
				if (printed >= 500)
					break;
			}
		}
	}
}

void solve()
{

}

int main()
{
	freopen("C-hard.out", "w", stdout);
	std::cout << "Case #1:\n";
	generate();
	int counter = 0;
	for (auto it = m.begin(); it != m.end() && counter < 500; ++it)
	{
		for (int i = 0; i < it->second.size() && counter < 500; ++i)
		{
			for (int j = i; j < it->second.size(); ++j)
			{
				std::cout << it->second[i] + it->second[j];
				for (int k = 0; k < it->first.size(); ++k)
					std::cout << ' ' << it->first[k];
				std::cout << std::endl;
				++counter;
			}
		}
	}
	/*for (int length = max_length; length <= max_length; ++length)
	{
		for (auto it = generated[length].begin(); it != generated[length].end(); ++it)
			cout << *it << ' ';
		cout << endl << endl;
	}
	rand(time(NULL));
	int t;
	cin >> t;

	for (int test_case = 1; test_case <= t; ++test_case)
	{
		printf("Case #%d:\n", test_case);
		read();
		solve();
	}
	*/
}