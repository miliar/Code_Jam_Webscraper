// CodeJam16.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>

using namespace std;

int getNumDigits(int n)
{
	int res = 0;
	while(n > 0)
	{
		n /= 10;
		res += 1;
	}
	return res;
}

bool hasDigit(int n, int digit)
{
	while(n > 0)
	{
		if ((n)%10 == digit)
			return true;
		n /= 10;
	}
	return false;
}

int getLeastNumberForI(int maxMultiple, int number, int digit)
{
	int res = maxMultiple;
	for(int i = maxMultiple; i >= 1; i--)
	{
		if(hasDigit(number*i, digit))
			res = i;
	}
	return res*number;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int t,n;
	cin >> t;
	FILE*fin, *fout;
	freopen_s(&fin, "input.txt", "r", stderr);
	freopen_s(&fout, "output.txt", "w", stderr);

	for(int i = 1; i <= t; i++)
	{
		cin >> n;
		if(n == 0)
		{
			fprintf_s(fout, "Case #%d: INSOMNIA\n",i);
			//cout << "INSOMNIA" << endl;
			continue;
		}
		int result = -1;
		
		for(int i = 0; i <= 9; i++)
		{
			
			int numdigits = getNumDigits(n);
			int tempResult;
			int startingEstimate;
			if(i == 0)
				startingEstimate = 10*n;
			else
				startingEstimate  = i*pow(10, numdigits);

			int multiple = startingEstimate/n ;
			if (startingEstimate%n != 0)
				multiple += 1;

			tempResult = getLeastNumberForI(multiple, n, i);
			if (tempResult == -1)
			{
				result = -1;
				break;
			}
			else
			{
				if (tempResult > result)
					result = tempResult;
			}

		}
		if (result == -1)
		{
			fprintf_s(fout, "Case #%d: INSOMNIA\n",i);
			//cout << "INSOMNIA" << endl;
		}
		else
		{
			fprintf_s(fout, "Case #%d: %d\n", i, result);
			//cout << result << endl;
		}
	}

	return 0;
}

