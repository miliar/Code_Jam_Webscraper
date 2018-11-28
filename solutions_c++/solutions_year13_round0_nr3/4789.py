// FairSquare.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool isPalindrome(__int64 number)
{
	int digits[200];

	__int64 tempNumber = number;
	int count = 0, d = 0;
	while(tempNumber)
	{
		d = tempNumber % 10;
		digits[count++] = d;
		tempNumber /= 10;
	}

	bool flag = true;
	int digitsToCheck = floor((float)count / 2);
	for (int idx = 0; idx <= digitsToCheck; ++idx)
	{
		if (digits[idx] != digits[count-1-idx])
		{
			flag = false;
			break;
		}
	}
	return flag;
}

void readCRLF(std::ifstream& fin)
{
	//char newline;
	//fin >> newline >> newline;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(argv[1], ios::binary);

	int cases = 0;
	fin >> cases;

	for (int i = 0; i<cases; ++i)
	{
		__int64 from =0, to=0, count = 0;
		
		fin >> from >> to;

		readCRLF(fin);

		__int64 sqrtFrom = 0, sqrtTo = 0;
		sqrtFrom	= ceil(sqrt((long double)from));
		sqrtTo		= floor(sqrt((long double)to));

		for (__int64 idx = sqrtFrom; idx <= sqrtTo; ++idx)
		{
			if (isPalindrome(idx) && isPalindrome(idx*idx))
				count++;
		}

		std::cout << "Case #" << i+1 << ": " << count << std::endl;

		if (i != cases-1)
			readCRLF(fin);
	}
}

