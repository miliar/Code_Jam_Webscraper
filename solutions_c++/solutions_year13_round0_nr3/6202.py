// GoogleCJ1Prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

const string inputFileName = "C:\\Users\\Karan\\Desktop\\C-small-attempt0.in";
const string outputFileName  = "C:\\Users\\Karan\\Desktop\\outputcsmall.txt";

bool IsFair(long x);

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(inputFileName);
	ofstream fout(outputFileName, ios::trunc);

	int T;

	fin>>T;

	for (int testCase = 1; testCase <= T; testCase++)
	{
		long lowerLimit, upperLimit;
		long lowerRoot, upperRoot;
		int answer = 0;

		fin>>lowerLimit>>upperLimit;

		lowerRoot = (long) ceill(sqrtl(lowerLimit));
		upperRoot = (long) floorl(sqrtl(upperLimit));

		cout<<lowerLimit<<" to "<<upperLimit<<endl;
		cout<<lowerRoot<<" to "<<upperRoot<<endl;

		for (int currentRoot = lowerRoot; currentRoot <= upperRoot; currentRoot++)
		{
			if (IsFair(currentRoot))
			{
				cout<<"---------";
				if (IsFair(currentRoot * currentRoot))
				{
    				answer++;
				}
			}
		}

		// End of Loop
		cout<<"Case #"<<testCase<<": "<<answer<<endl;
		fout<<"Case #"<<testCase<<": "<<answer<<endl;

	}
	
	
	
	
	// The END
	getchar();
	return 0;
}

bool IsFair(long x)
{
	int num, reverse;
	if (x < 10)
	{
		return true;
	}
	if (x%10 == 0)
	{
		return false;
	}

	num = x;
	reverse = 0;
	while (num > 0)
	{
		reverse = reverse * 10 + (num%10);
		num = num/10;
	}
	cout<<"Number is "<<x<<" and reverse is "<<reverse<<endl;
	return (x == reverse);
}