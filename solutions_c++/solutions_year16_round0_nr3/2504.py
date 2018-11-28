// ProblemC.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define ll long long
#define vll vector<ll>

ll toDecimal(ll n, int b)
{
	ll result = 0;
	ll multiplier = 1;

	while (n>0)
	{
		ll x = n & 1;
		result += x * multiplier;
		multiplier *= b;
		n = n >> 1;
	}

	return result;
}

ll getDivisor(ll num)
{
	if (num <= 2) return 1;
	if (num % 2 == 0) return 2;
	
	ll m = sqrt(num);
	for (int i = 3; i <= m; i += 2)
		if (num%i == 0)
			return i;

	return 1;
}

string toString(ll num)
{
	string result;
	while (num > 0)
	{
		if (num & 1)
			result = "1" + result;
		else
			result = "0" + result;
		num = num >> 1;
	}

	return result;
}

int main()
{
	ofstream fout("C-small-attempt0.out");
	fout << "Case #1:" << endl;
	int k = 50;

	ll start_num = 32769;//1000 0000 0000 0001
	while (k > 0)
	{
		bool pass = true;
		vll divisor_base(11, 0);
		for (int i = 2; i <= 10; i++)
		{
			ll decimal = toDecimal(start_num, i);
			ll divisor = getDivisor(decimal);

			if (divisor == 1)
			{
				pass = false;
				break;
			}

			divisor_base[i] = divisor;
		}

		if (pass)
		{
			k--;
			//print result;
			fout << toString(start_num).c_str();
			for (int i = 2; i <= 10; i++)
			{
				fout << " " << divisor_base[i];
			}
			fout << endl;
		}

		start_num += 2;
	}

    return 0;
}

