// C. Fair and Square.cpp : 定义控制台应用程序的入口点。
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

// 判断是否为回文数字
bool IsPalindrom(double& fDigit)
{
	bool bResult = false;

	char szDigitSrc[110] = { 0 };

	DoubleToString(szDigitSrc, fDigit);

	// 判断字符串是否回文
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

// 判断一个数是否为平方数字
bool IsSquareNum(double& fDigit)
{
	bool bResult = false;

	char szDigitSrc[110] = { 0 };
	char szDigitConvert[110] = { 0 };

	// 首先判断是否为平方数
	double fSqrt = sqrt(fDigit);

	// 首先通过字符串判断是否为平方数
	DoubleToString(szDigitSrc, fSqrt);
	int nLen = strlen(szDigitSrc);
	// 字符串乘以10
	szDigitSrc[nLen] = '0';


	// 数值乘以10后再转成字符串后比较
	fSqrt *= 10; 
	DoubleToString(szDigitConvert, fSqrt);

	if(strcmp(szDigitConvert, szDigitSrc) == 0)
	{
		// fSqrt 为整数， 同时fDigit为平方数

		fSqrt /= 10;

		// 判断 fSqrt 是否回文
		bResult = IsPalindrom(fSqrt);
	}

	return bResult;
}

double GetSquareAndPalindromeInterval(double& nBegin, double& nEnd)
{
	double fResult = 0;

	while(nBegin <= nEnd)
	{
		// 判断是否为回文数字或者平方数字
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

	// 输入次数
	fscanf(pFile, "%d\n", &nTimes);
	for (i = 0; i < nTimes; i ++)
	{
		fscanf(pFile, "%lf %lf", &fA, &fB);

		szOutputArray[i] = GetSquareAndPalindromeInterval(fA, fB);
	}
	fclose(pFile);


	// 输出
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