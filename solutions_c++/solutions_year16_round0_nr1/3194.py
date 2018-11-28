// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <cassert>
using namespace std;
#define _CRT_SECURE_NO_WARNINGS
unsigned int hash_tbl[10] = { 0 };

void set_freq(unsigned long long num)
{
	do
	{
		hash_tbl[num % 10]++;
		num /= 10;
	} while (num != 0);
}

unsigned int success()
{
	for (unsigned int i = 0; i < 10; ++i)
	{
		if (0 == hash_tbl[i])
		{
			return 0;
		}
	}
	return 1;
}

void clear_hash()
{
	for (unsigned int i = 0; i < 10; ++i)
	{
		hash_tbl[i] = 0;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = NULL;
	FILE* out = NULL;
	errno_t fin = freopen_s(&in, "A-large.in", "r", stdin);
	assert(0x0 == fin);
	errno_t fout = freopen_s(&out, "A-large.out", "w", stdout);
	assert(0x0 == fout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		clear_hash();
		int i = 1;
		unsigned int num;
		unsigned long long result;
		cin >> num;
		if (num != 0)
		{
			do
			{
				result = num * i;
				set_freq(result);
				i++;
			} while (0x1 != success());

			cout << "Case #" << t << ": " << result << endl;
		}
		else
		{
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;
}

