// 2Task.cpp: определяет точку входа для консольного приложения.
//

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
#include <cstdio>

//#define _CRT_SECURE_NO_WARNINGS
//#define _SECURE_SCL 2

using namespace std;

bool MethodPol(string str)
{
	bool bFlag = false;
	for(long j = 0; j<str.length(); j++)
	{
		if(str[j] == str[str.length()-j-1])
			bFlag = true;
		else
		{
			bFlag = false;
			break;
		}
	}
	return bFlag;
}

int main()
{
	ifstream file("C-small-attempt0.in");
	ofstream offile("output.txt");

	int N = 0;

	file>>N;
	string str = "";
	__int64 A = 0;
	__int64 B = 0;
	__int64 Count = 0;
	char stringChar[14];

	// цикл по тестам
	for(int iN=0; iN<N; iN++)
	{
		file>>A;
		file>>B;
		for(__int64 i = A; i<=B; i++)
		{
			sprintf(stringChar, "%lld", i);
			str = stringChar;
			bool bFlag = false;

			// проверка самого числа
			bFlag = MethodPol(str);

			if(bFlag)
			{
				double kor = sqrt(i);
				bool bF = false;
				char stringChar2[14];
				string str1;

				if(kor - (__int64)kor == 0) 
				{
					sprintf(stringChar2, "%lld", (__int64)kor);
					str1 = stringChar2;
					bF = MethodPol(str1);
				}
				if(bF)
				{
					Count++;
				}
			}
		}
		offile<<"Case #"<<iN+1<<": "<<Count<<endl;
		Count = 0;
	}
	int n;
	cin>>n;

	return 0;
}


