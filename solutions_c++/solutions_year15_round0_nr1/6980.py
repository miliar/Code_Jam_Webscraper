// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int testcase = 0;
	int Max = 0;
	
	cin >> testcase;

	for (int i = 0; i < testcase; i++)
	{
		string dataset;
		int AddP = 0;
		int sum = 0;
		cin>> Max;
		cin>> dataset;
		for (int j = 0; j < Max + 1; j++)
		{
			if (sum < j)
			{
				AddP = AddP + j - sum;
				sum = j;
			}
			sum = sum + (dataset[j] - '0');
		}
		cout << "Case #" << (i + 1) << ": " << AddP<<endl;
		string garbage;
		getline(cin, garbage);

	}
	return 0;
}

