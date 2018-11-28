
#include <iostream>
#include "uint128_t.h"
#include <bitset>
using namespace std;

//uint128_t values for [base][bit_location (zero-based)]
uint128_t bitValues[11][32];

bool isPrime(uint128_t number, uint128_t &divisor)
{
	if (number == 2 || number == 3) return true;
	else
	{
		//Choose higher number to get more jam coins.
		uint128_t upperBound = 100;

		/*
		if (number.upper() == 0)
			upperBound = uint128_t((uint64_t)(sqrt(number.lower()) + 1));
		else
			upperBound = uint128_t(number / 2);
		*/

		for (uint128_t c(2); c <= upperBound; c++)
		{ 
			if ((number % c) == 0) 
			{
				divisor = c;
				return false;
			}
		}

		return true;
	}
}

uint128_t coinValue(uint32_t coinBits, int base)
{
	uint128_t returnValue;

	for (int b = 0; b < 32; b++)
		if(coinBits & ((uint32_t)1) << b)
			returnValue += bitValues[base][b];

	return returnValue;
}

 

int main()
{
	
	int tCount, N, J;
	cin >> tCount;
	cin >> N;
	cin >> J;

	cout << "Case #1:" << endl;
		
	//Precompute bit values

	for (int base = 2; base <= 10; base++)
		for(int b=0; b<32; b++)
		{
			bitValues[base][b] = 1;
			for (int m = 0; m < b; m++)
				bitValues[base][b] *= uint128_t(base);
		}

	uint32_t jamCoinMiddleMax = pow(2, N - 2) - 1;

	int foundCount = 0;

	for (uint32_t jamCoinMiddle = 0; jamCoinMiddle <= jamCoinMiddleMax; jamCoinMiddle++) //Try all candidates
	{
		uint32_t coinCandidate = (1 << (N - 1)) | jamCoinMiddle << 1 | 1;
		bool validCandidate = true;
		uint128_t divisor[11];

		for (int base = 2; base <= 10; base++) //Check all bases
		{
			uint128_t value = coinValue(coinCandidate, base);
			if (isPrime(value, divisor[base]))
			{
				validCandidate = false;
				break;
			}
		}

		if (validCandidate)
		{
			bitset<32> a(coinCandidate);
			for (int i = N-1; i >= 0; i--)
				cout << (int)a[i];

			cout << " ";

			for (int base = 2; base <= 10; base++)
			{
				//cout << divisor[base] << "(" << coinValue(coinCandidate, base) << ")";
				cout << divisor[base];
				cout << " ";
			}
			
			cout << endl;

			foundCount++;

			if (foundCount >= J) return 0;
		}
	}

	cout << "Error, enough coins were not found!";
	
	
	return 0;
}

