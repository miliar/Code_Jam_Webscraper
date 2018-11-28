#include <iostream>
#include <string>

using namespace std;

bool arrTemp[100];

typedef struct _CaseStruct
{
	int nLength;
	bool arrCase[100];
} CaseStruct;

int findFirstUp(CaseStruct* csCase)
{
	for (int i = 0; i < csCase->nLength; i++)
	{
		if (csCase->arrCase[i])
		{
			return i;
		}
	}

	return csCase->nLength;
}

void solveCase(CaseStruct* csCase)
{
	int nNumOfFlips = 0;
	int nLastIndex = csCase->nLength - 1;
	int nFirstUp;
	int i;
	int j;

	while ((nLastIndex >= 0) && (csCase->arrCase[nLastIndex]))
	{
		nLastIndex--;
	}

	while (nLastIndex >= 0)
	{
		nFirstUp = findFirstUp(csCase);

		if (0 == nFirstUp)
		{
			j = 0;

			while ((j < nLastIndex) && (csCase->arrCase[j]))
			{
				csCase->arrCase[j] = !csCase->arrCase[j];
				j++;
			}
		}
		else
		{
			for (i = 0; i <= nLastIndex; i++)
			{
				arrTemp[i] = csCase->arrCase[i];
			}

			for (i = 0; i <= nLastIndex; i++)
			{
				csCase->arrCase[i] = !arrTemp[nLastIndex - i];
			}

			nLastIndex -= nFirstUp;
		}

		nNumOfFlips++;
	}

	cout << nNumOfFlips << endl;
}

int main()
{
	int nCasesNum;
	CaseStruct arrCases[100];
	string szCase;
	int j;

	cin >> nCasesNum;

	for (int i = 0; i < nCasesNum; i++)
	{
		cin >> szCase;

		arrCases[i].nLength = szCase.length();

		for (j = 0; j < arrCases[i].nLength; j++)
		{
			arrCases[i].arrCase[j] = ((szCase[j] == '+') ? true : false);
		}
	}

	for (j = 0; j < nCasesNum; j++)
	{
		cout << "Case #" << j + 1 << ": ";
		solveCase(&arrCases[j]);
	}
}