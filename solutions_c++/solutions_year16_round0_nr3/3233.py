#include "stdafx.h"
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <stdio.h>

#include <math.h>

using namespace std;

ofstream fout("OUT111.txt");
ifstream fin("INP111.txt");

int len = 16;
int number = 50;

long long div(long long x)
{
	long long y = 2;
	while (y*y <= x)
	{
		if (x%y == 0)
			return y;
		y++;
	}

	return 0;
}

string toBinary(long long x)
{
	string s = "";
	while (x > 0)
	{
		int rem = x % 2;
		if (rem == 1)
			s = s + "1";
		else
			s = s + "0";
		x = (x - rem) / 2;
	}
	while (s.size() < len - 2)
		s = s + "0";

	reverse(s.begin(), s.end());
	return s;
}

long long toBase(long long val, long long base)
{
	long long res = 0;
	long long mult = base;
	while (val > 0)
	{
		int rem = val % 2;
		if (rem == 1)
			res = res + mult;

		val = (val - rem) / 2;
		mult = mult*base;
	}

	return res;
}

int main() 
{
	int found = 0;
	long long add[11];
	for (long long i = 2; i <= 10; i++)
	{
		long long res = 1;
		for (int j = 0; j < len - 1; j++)
			res = res*i;

		add[i] = res + 1;
	}

	fout << "Case #1:" << "\n";

	long long step = 0;
	while (found < number)
	{
		long long divs[11];
		bool foundPrime = false;
		for (long long i = 2; i <= 10 && !foundPrime; i++)
		{
			divs[i] = div(add[i] + toBase(step, i));
			if (divs[i] == 0)
				foundPrime = true;
		}

		if (!foundPrime)
		{
			found++;

			string s = "1" + toBinary(step) + "1";

			if (1)
			{
				fout << s;
				for (int i = 2; i <= 10; i++)
					fout << " " << divs[i];
				fout << "\n";
			}

			if (0)
			{
				for (long long i = 2; i <= 10; i++)
				{
					long long res = 0;
					long long mult = 1;
					for (int j = len - 1; j >= 0; j--)
					{
						if (s[j] == '1')
							res += mult;

						mult = mult*i;
					}

					if (res%divs[i] != 0)
						fout << s << " " << i << " " << res << " " << divs[i] << "\n";
				}
			}
		}

		step++;
	}

	return 0;
}

