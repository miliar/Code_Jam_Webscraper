// CoinJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include<bitset>
using namespace std;

string base(int x, int b)
{
	string res;
	do
	{
		res.append(to_string(x % b));
		x /= b;
	} while (x != 0);
	reverse(res.begin(), res.end());
	return res;
}

unsigned long long isPrime(unsigned long long x)
{
	for (long long int k = 2; k <= sqrt(x); k++)
	{
		if (x % k == 0)
		{
			return k;
		}
	}
	return 0;
}

void compute(int N, int J, ofstream &out)
{
	int jamcoins = 0;
	int start = pow(2, N - 1) - 1;
	while (jamcoins < J)
	{
		bool cont = false;
		string divisors = "";
		start += 2;
		string jamcoin = base(start, 2);
		for (int i = 2; i <= 10; i++)
		{
			unsigned long long x = strtoull(jamcoin.c_str(),NULL, i);
			unsigned long long div = isPrime(x);
			if (div == 0)
			{
				cont = true;
				break;
			}
			else
			{
				divisors.append(" ");
				divisors.append(to_string(div));
			}
		}
		if (cont)
			continue;
		out << jamcoin << divisors << endl;
		jamcoins++;
	}
}

int main()
{
	ifstream input("input.in");
	if (input.is_open())
	{
		int T;
		ofstream output("output.out");
		input >> T;
		for (int i = 1; i <= T; i++)
		{
			int N, J;
			input >> N >> J;
			output << "Case #" << i << ": " << endl;
			compute(N, J, output);
		}
		input.close();
		output.close();
	}
	return 0;
}