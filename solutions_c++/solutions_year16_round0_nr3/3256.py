// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

unsigned long long convert(unsigned short x, unsigned short basis)
{
	unsigned long long res = 0;
	for (unsigned short i = 0; i < 16; i++)
	{
		res += pow(basis, i) * ((x >> i) & 0x0001);
	}
	return res;
}

bool check_prime(unsigned long long x, unsigned long long & divider)
{
	//if (x % 2 == 0) return false;
	for (unsigned long long i = 3; i < sqrt(x); i+=2)
	{
		if (x % i == 0)
		{
			divider = i;
			return false;
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("c.in");
	ofstream fo("c_small.out");

	int t,n,j;
	fi >> t >> n >> j;

	unsigned short p = 32767;
	//unsigned int p = 2147483647;

	int cnt = 0;
	fo << "Case #1:" << endl;
	while (cnt < j)
	{
		p += 2;
		bool is_prime = false;
		vector<unsigned long long> dividers;
		for (int i = 2; i <= 10; i++)
		{
			unsigned long long div;
			if (check_prime(convert(p, i), div))
			{
				is_prime = true;
				break;
			}
			else
			{
				dividers.push_back(div);
			}
		}
		if (!is_prime)
		{
			for (int i = 0; i < n; i++)
			{
				fo << (((p << i) & 0x8000) > 0 ? '1' : '0');
			}
			fo << " ";
			for (int i = 0; i < 8; i++)
			{
				fo << (unsigned int)dividers[i] << " ";
			}
			fo << (unsigned int)dividers[8] <<endl;
			cnt++;
		}
	}

	fi.close();
	fo.close();

	return 0;
}

