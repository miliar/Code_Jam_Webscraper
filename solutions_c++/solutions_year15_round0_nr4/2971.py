// Problem D. Ominous Omino-smallsize.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>  

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("D-small-attempt0.in");
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

	vector<string> result;
	int T;
	input >> T;
	input.get();

	for (int i = 0; i < T; i++)
	{
		int XRC[3] = { 0 };
		input >> XRC[0] >> XRC[1] >> XRC[2];
		input.get();

		if (XRC[0] == 1)
		{
			result.push_back("GABRIEL");
			continue;
		}
		else if (XRC[0] == 2)
		{
			if (XRC[1] % 2 == 1 && XRC[2] % 2 == 1)
			{
				result.push_back("RICHARD");
				continue;
			}
			else
			{
				result.push_back("GABRIEL");
				continue;
			}
		}
		else if (XRC[0] == 3)
		{
			if (XRC[1] == 1 || XRC[2] == 1)
			{
				result.push_back("RICHARD");
				continue;
			}
			else if (XRC[1] % 3 != 0 && XRC[2] % 3 != 0)
			{
				result.push_back("RICHARD");
				continue;
			}
			else
			{
				result.push_back("GABRIEL");
				continue;
			}
		}
		else   //XRC[0] == 4
		{
			if (XRC[1]<3 || XRC[2]<3)
			{
				result.push_back("RICHARD");
				continue;
			}
			else if (XRC[1] % 4 == 0 || XRC[2]%4==0)
			{
				result.push_back("GABRIEL");
				continue;
			}
			else
			{
				result.push_back("RICHARD");
				continue;
			}
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

