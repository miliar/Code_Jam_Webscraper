#include <iostream>
#include <cmath>
#include <float.h>
#include <iomanip>

using namespace std;

#define N 16
#define J 50

double convertToDecimal(double dNum, int nBase)
{
	double dNewNum = 0;
	int i = 0;
	double dModulu;

	while (0 != dNum)
	{
		dModulu = fmod(dNum, 10);
		dNewNum += dModulu * pow(nBase, i);
		dNum = (dNum - dModulu) / 10;
		i++;
	}

	return dNewNum;
}

double convertDecimalToBinary(double dNum)
{
	double dNewNum = 0;
	double dModulu;
	double dMul = 1;

	while (0 != dNum)
	{
		dModulu = fmod(dNum, 2);
		dNewNum = dNewNum + dModulu * dMul;
		dNum = (dNum - dModulu) / 2;
		dMul *= 10;
	}

	return dNewNum;
}

double IsPrime(double dNum)
{
	if (0 == fmod(dNum, 2))
	{
		return 2;
	}
	else
	{
		for (double i = 3; i * i <= dNum; i += 2)
		{
			if (0 == fmod(dNum, i))
			{
				return i;
			}
		}
	}

	return 0;
}

int main()
{
	double dDecimal;
	double dBinary;
	int nCount = 0;
	double arrDividers[9];
	int i;

	cout << fixed << setprecision(0);

	cout << "Case #1:" << endl;

	dDecimal = pow(2, N - 1) - 1;

	while (J > nCount)
	{
		dDecimal += 2;
		dBinary = convertDecimalToBinary(dDecimal);

		for (i = 0; i < 9; i++)
		{
			arrDividers[i] = IsPrime(convertToDecimal(dBinary, i + 2));

			if (0 == arrDividers[i])
			{
				break;
			}
		}

		if (9 == i)
		{
			cout << dBinary;

			for (i = 0; i < 9; i++)
			{
				cout << " " << arrDividers[i];
			}

			cout << endl;

			nCount++;
		}
	}
}