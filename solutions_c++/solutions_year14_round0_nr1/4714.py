// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
 
using namespace std;

std::ifstream infile("in.txt");
std::ofstream outfile("out.txt");

int T;

void doit()
{
	infile >> T;
	cout << "T = " << T << endl;
	for (int i = 0; i < T; ++i)
	{
		int first, second;
		int num1[4][4];
		int num2[4][4];

		infile >> first;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				infile >> num1[j][k];
			}
		}

		infile >> second;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				infile >> num2[j][k];
			}
		}

		int sameNum = 0;
		int magic;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if (num1[first - 1][j] == num2[second - 1][k])
				{
					sameNum++;
					magic = num1[first - 1][j];
				}
			}
		}

		outfile << "Case #" << i + 1 << ": ";
		if (sameNum == 1)
		{
			outfile << magic<<endl;
		}
		else if (sameNum > 1)
		{
			outfile << "Bad magician!"<<endl;
		}
		else
			outfile << "Volunteer cheated!"<<endl;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	doit();
	return 0;
}

