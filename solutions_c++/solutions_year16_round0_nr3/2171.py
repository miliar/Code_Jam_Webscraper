// Coin Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>;
#include <string>

using namespace std;
const int P_SIZE = 12;
int primes[P_SIZE] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 };
int factors[9] = {};
char* lltoa(long long val, int base) {
	static char buf[64] = { 0 };
	int i = 62;
	int sign = (val < 0);
	if (sign) val = -val;
	if (val == 0) return "0";
	for (; val && i; --i, val /= base) {
		buf[i] = "0123456789abcdef"[val % base];
	}
	if (sign) {
		buf[i--] = '-';
	}
	return &buf[i + 1];
}
int main()
{
	long long num = 1000000000000001;
	cout << "Case #1: "<< endl;
	int count = 0;
	while (count < 50)
	{
		bool isjamcoin = true;
		for (int i = 2; i < 11; i++)
		{
			long long n = stoll(to_string(num), 0, i);
			bool prime = true;
			for (int j = 0; j < P_SIZE; j++)
			{
				if (n%primes[j] == 0)
				{
					prime = false;
					factors[i - 2] = primes[j];
					break;
				}
			}
			if (prime)
			{
				isjamcoin = false;
				break;
			}
		}
		if (isjamcoin)
		{
			cout << num;
			for (int i = 0; i < 9; i++)
			{
				cout << " " << factors[i];
			}
			cout << endl;
			count++;
		}
		num = stoll(lltoa(stoll(to_string(num), 0, 2)+2, 2), 0, 10);
	}
	
}

