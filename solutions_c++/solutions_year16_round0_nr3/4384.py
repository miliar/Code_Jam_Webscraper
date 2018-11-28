#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

void incr(int *part, int l)
{
	for (int i = l - 2; i > 0; i--)
	{
		if (part[i] == 0)
		{
			part[i] = 1;
			break;
		}
		part[i] = 0;
	}
}

__int64 isPrime(__int64 num)
{
	__int64 range = __int64(sqrt(num));
	__int64 mdiv = 1;
	__int64 i;

	if (num % 2 != 0)
	{
		for (i = 3; i <= range; i += 2)
		{
			if (num%i == 0)
			{
				mdiv = i;
				break;
			}
		}
	}
	else
	{
		if (num != 2)
			mdiv = 2;
	}

	return mdiv;
}

int main()
{
	int ncases, n, j;
	int* coin;
	__int64 num;
	__int64 divs[9];

	ifstream in;
	ofstream out;
	in.open("C/C-small-attempt0.in");
	out.open("C/C-small-results.out");

	in >> ncases;
	in >> n >> j;
	coin = (int*)malloc(sizeof(int)*n);
	memset(coin, 0, sizeof(int)*n);
	coin[0] = 1;
	coin[n - 1] = 1;

	out << "Case #1: " << endl;
	for (int t = 0; t < j; t++)
	{
		for (;;)
		{
			memset(divs, 0, sizeof(__int64) * 9);

			for (int i = 2; i <= 10; i++)
			{
				num = 0;
				for (int j = 0; j < n; j++)
					num += coin[j] * pow(i, j);

				divs[i - 2] = isPrime(num);

				if (divs[i - 2] == 1)
					break;
			}

			if (divs[8] <= 1)
			{
				incr(coin, n);
			}
			else
			{
				incr(coin, n);
				break;
			}
		}

		//print result
		out << num;
		for (int l = 0; l < 9; l++)
			out << " " << divs[l];

		if (t < j - 1)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}