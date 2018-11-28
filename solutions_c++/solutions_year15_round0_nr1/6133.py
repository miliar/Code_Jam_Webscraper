// GoogleJam1-smalltest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>  

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("A-large.in");
	ofstream output("result.txt");

	if (!input)
	{
		cout << "Unable to open input";
		exit(1);
	}

	if (!output)
	{
		cout << "Unable to open output";
		exit(1);
	}


	int T;
	input >> T;
	input.get();

	vector<int> result;

	

	for (int i = 0; i < T; i++)
	{
		int Smax;
		input >> Smax;
		int * audienceARR = new int[Smax];

		char garbage = input.get();

		for (int j = 0; j <= Smax; j++)
		{
			audienceARR[j] = input.get() - '0';
		}
		input.get();
	
		if (Smax == 0)
		{
			result.push_back(0);
			continue;
		}
		else
		{
			int sum = 0;
			int friendaud = 0;
			for (int j = 1; j <= Smax; j++)
			{
				sum += audienceARR[j - 1];
				if (sum+friendaud < j)
				{
					friendaud = j - sum;
				}
			}
			result.push_back(friendaud);
		}
	}

	for (int i = 0; i < T; i++)
	{
		output << "Case #" << i + 1 << ": " << result[i] << endl;
	}

	cout << "Finished" << endl;
	cin.get();
	return 0;
}

