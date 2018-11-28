// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cstring>
using namespace std;

long long GetNumberInBase(long long n, int base)
{
	long long r = 0;
	long long p = 1;
	while (n)
	{
		r += (n % 10)*p;
		p *= base;
		n /= 10;
	}
	return r;
}

long long GetNumberInBaseTwo(long long n)
{
	long long r = 0;
	long long p = 1;
	while (n)
	{
		r += (n % 2)*p;
		p *= 10;
		n /= 2;
	}
	return r;
}

long long IsPrime(long long n)
{
	if (n == 1) return -1;
	if (n == 2) return -1;
	if (n % 2 == 0) return 2;
	for (long long j = 3; j*j <= n; j += 2)
	{
		if (n % j == 0)
		{
			return j;
		}
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin >> t;

	int N;
	cin >> N;

	int J;
	cin >> J;

	// 2^16*A + A = A(2^16+1)
	// 3^16*A + A = A(3^16+1)
	// and so on

	long long p = (long long)pow(2.0, 15);
	long long q = (int)pow(2.0, 16);
	int cnt = 0;
	long long D[11];
	long long numBase[11];
	cout << "Case #1:\n";
	for (long long i = p; i < q; i++)
	{
		long long coin = GetNumberInBaseTwo(i);
		long long d10 = IsPrime(coin);
		long long d2 = IsPrime(i);
		if ((coin % 2 == 1) && (d10 != -1) && (d2 != -1))
		{
			bool isJamCoin = true;
			D[2] = d2;
			D[10] = d10;
			numBase[2] = i;
			numBase[10] = coin;
			for (int j = 3; j < 10; j++)
			{
				long long numInBase = GetNumberInBase(coin, j);
				numBase[j] = numInBase;
				D[j] = IsPrime(numInBase);
				if (D[j] == -1)
				{
					isJamCoin = false;
					break;
				}
			}
			if (isJamCoin)
			{
				cout << coin << coin << " ";
				for (int j = 2; j <= 10; j++)
				{
					cout << numBase[j] << " ";
				}
				cout << "\n";
				cnt++;
				if (cnt == J)
				{
					break;
				}
			}
		}
	}
	return 0;
}

