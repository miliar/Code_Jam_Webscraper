// prob3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <cmath>
#include <vector>
using namespace std;

bool IS_prime(unsigned long long num, vector<unsigned long long> &arr, unsigned int base)
{
	for (unsigned long long i = 2; i <= sqrt(num); ++i)
	{
		//if (i % 2 == 0)
		//	i++;

		if (0 == ((num) % i))
		{
			vector<unsigned long long>::iterator it;
			it = find(arr.begin(), arr.end(), i);
			if (it == arr.end())
			{
				arr[base-2] = i;
				return false;
			}
		}
	}

	return true;
}

unsigned long long convert_to_base(string num, unsigned int base)
{
	unsigned long long result = 0;
	unsigned int len = num.length();
	for (int i = 0; i < (int)(len-1); ++i)
	{
		unsigned long long a = num[i];
		result += (unsigned long long)pow(base * (num[i] - '0'), len - 1 - i);
	}
	result += (num[len-1] - '0');
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//
	//std::cout << binary << "\n";

	//unsigned long decimal = std::bitset<8>(binary).to_ulong();
	//std::cout << decimal << "\n";
	FILE* in = NULL;
	FILE* out = NULL;
	errno_t fin = freopen_s(&in, "C-small-attempt0.in", "r", stdin);
	assert(0x0 == fin);
	errno_t fout = freopen_s(&out, "C-small.out", "w", stdout);
	assert(0x0 == fout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << T << ":" << endl;
		unsigned int N, J;
		cin >> N >> J;
		for (unsigned int i = (unsigned int) pow(2, N - 2); (J > 0) && (i < (unsigned long long) pow(2, N-1)); ++i)
		{
			unsigned int i2 = (i << 1) | 1;
			unsigned int base;
			std::string binary = std::bitset<32>(i2).to_string(); //to binary
			binary.erase(0, binary.find_first_not_of('0'));
			vector<unsigned long long> arr(9, 0);
			for (base = 2; base <= 10; ++base)
			{
				unsigned long long basenum = convert_to_base(binary, base);
				//unsigned long long div;
				
				if (true == IS_prime(basenum, arr, base))
				{
					break;
				}
			}
			if (base > 10)
			{
				J--;
				cout << binary;
				for (unsigned int base = 2; base <= 10; ++base)
				{
					cout << " " << arr[base - 2];
				}
				cout << endl;
			}
		}
	}
	return 0;
}
