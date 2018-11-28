#include <iostream>

using namespace std;

bool arrDigits[10];
int nCurrentCase = 1;
int nCheckedDigits;

bool checkDigits(int nNum)
{
	int nDigit;

	while (0 != nNum)
	{
		nDigit = nNum % 10;

		if (false == arrDigits[nDigit])
		{
			arrDigits[nDigit] = true;
			nCheckedDigits++;
			
			if (10 == nCheckedDigits)
			{
				return true;
			}
		}

		nNum /= 10;
	}

	return false;
}

void solveCase(int nNum)
{
	if (0 == nNum)
	{
		cout << "Case #" << nCurrentCase << ": INSOMNIA" << endl;
	}
	else
	{
		int nOriginalNum = nNum;

		while (!checkDigits(nNum))
		{
			nNum += nOriginalNum;
		}

		cout << "Case #" << nCurrentCase << ": " << nNum << endl;
	}
}

void zeroArray()
{
	for (int i = 0; i < 10; i++)
	{
		arrDigits[i] = false;
	}
}

int main()
{
	int nCaseNum;
	int* arrInputs;

	cin >> nCaseNum;

	arrInputs = new int[nCaseNum];

	for (int i = 0; i < nCaseNum; i++)
	{
		cin >> arrInputs[i];
	}

	for (; nCurrentCase <= nCaseNum; nCurrentCase++)
	{
		zeroArray();
		nCheckedDigits = 0;
		solveCase(arrInputs[nCurrentCase - 1]);
	}

	delete[] arrInputs;
}