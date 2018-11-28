// C. Fair and Square.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

// output Array
double szOutputArray[100] = { 0 };

void DoubleToString(char* pOutputBuf, double& fDigit)
{
	int dec, sign; 
	char* pBuf = ecvt(fDigit, 10, &dec, &sign);
	pBuf = ecvt(fDigit, dec, &dec, &sign);

	strcpy(pOutputBuf, pBuf);
}

// �ж��Ƿ�Ϊ��������
bool IsPalindrom(double& fDigit)
{
	bool bResult = false;

	char szDigitSrc[110] = { 0 };

	DoubleToString(szDigitSrc, fDigit);

	// �ж��ַ����Ƿ����
	int nEnd = strlen(szDigitSrc) - 1;
	int nBegin = 0;

	while(nBegin < nEnd)
	{
		if (szDigitSrc[nBegin] != szDigitSrc[nEnd])
		{
			break;
		}

		nBegin ++;
		nEnd --;
	}

	if (nBegin >= nEnd)
	{
		bResult = true;
	}

	return bResult;
}

// �ж�һ�����Ƿ�Ϊƽ������
bool IsSquareNum(double& fDigit)
{
	bool bResult = false;

	char szDigitSrc[110] = { 0 };
	char szDigitConvert[110] = { 0 };

	// �����ж��Ƿ�Ϊƽ����
	double fSqrt = sqrt(fDigit);

	// ����ͨ���ַ����ж��Ƿ�Ϊƽ����
	DoubleToString(szDigitSrc, fSqrt);
	int nLen = strlen(szDigitSrc);
	// �ַ�������10
	szDigitSrc[nLen] = '0';


	// ��ֵ����10����ת���ַ�����Ƚ�
	fSqrt *= 10; 
	DoubleToString(szDigitConvert, fSqrt);

	if(strcmp(szDigitConvert, szDigitSrc) == 0)
	{
		// fSqrt Ϊ������ ͬʱfDigitΪƽ����

		fSqrt /= 10;

		// �ж� fSqrt �Ƿ����
		bResult = IsPalindrom(fSqrt);
	}

	return bResult;
}

double GetSquareAndPalindromeInterval(double& nBegin, double& nEnd)
{
	double fResult = 0;

	while(nBegin <= nEnd)
	{
		// �ж��Ƿ�Ϊ�������ֻ���ƽ������
		if (IsPalindrom(nBegin) && IsSquareNum(nBegin))
		{
			fResult ++;
		}

		nBegin ++;
	}

	return fResult;
}

int main()
{
	int nTimes, i;
	double fA, fB;

	FILE* pFile = fopen("C-small-attempt1.in", "r");

	// �������
	fscanf(pFile, "%d\n", &nTimes);
	for (i = 0; i < nTimes; i ++)
	{
		fscanf(pFile, "%lf %lf", &fA, &fB);

		szOutputArray[i] = GetSquareAndPalindromeInterval(fA, fB);
	}
	fclose(pFile);


	// ���
	pFile = fopen("output.txt", "w");
	for (i = 0; i < nTimes; i ++)
	{
		char szDigitSrc[110] = { 0 };
		DoubleToString(szDigitSrc, szOutputArray[i]);
		if (szOutputArray[i] < 0.0000001 && szOutputArray[i] > -0.0000001)
		{
			szDigitSrc[0] = '0';
		}

		fprintf(pFile,"Case #%d: %s\n", i + 1, szDigitSrc);
	}

	fclose(pFile);
	return 0;
}