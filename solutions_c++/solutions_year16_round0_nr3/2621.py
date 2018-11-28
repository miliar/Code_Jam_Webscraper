#include <iostream>
#include <fstream>
#include <limits>
#include <string>
#include <set>

typedef unsigned long long Number;

Number find_n(std::string s)
{
	bool found[10] = {};
	int left = 10;
	int l = s.length();
	int res = 0;
	while (--l >= 0)
	{
		if (s[l] == '-')
		{
			++res;
			for (int n = 0; n <= l; ++n)
			{
				s[n] = s[n] == '-' ? '+' : '-';
			}
		}
	}
	return res;
}

int find_prime(long long n)
{
	if (n % 2 == 0)
		return 2;
	if (n % 3 == 0)
		return 3;
/*
	if (n % 5 == 0)
		return 5;
		*/
	if (n % 7 == 0)
		return 7;
//	if (n % 11 == 0)
//		return 11;
	return 0;
}

int main()
{
	int n_found = 1;
	std::cout << "Case #1:" << std::endl;
	std::set<std::string> known;
	for (;;)
	{
		std::string number = "1000000000000001";
		for (int k = 0; k < 4; ++k)
		{
			for (;;)
			{
				int i = rand() % 16;
				if(number[i] == '0')
				{
					number[i] = '1';
					break;
				}
			}
		}
		if (known.find(number) != known.end())
			continue;
		known.insert(number);
		int prime[11] = {};
		prime[10] = 3;
		bool found = true;
		for (int b = 2; b <= 9; ++b)
		{
			long long n = strtoll(number.c_str(), nullptr, b);
			prime[b] = find_prime(n);
			if (prime[b] == 0)
			{
				found = false;
				break;
			}
		}
		if (found)
		{
			std::cout << number;
			for (int b = 2; b <= 10; ++b)
				std::cout << " " << prime[b];
			std::cout << std::endl;
			++n_found;
		}
		if (n_found > 50)
			break;
	}

	return 0;
}