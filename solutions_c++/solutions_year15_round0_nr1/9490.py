// ConsoleApplication4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin;
	fin.open("C:\\Users\\ankulg\\Downloads\\A-large.in", ifstream::in);
	ofstream fout("c:\\users\\ankulg\\desktop\\result.txt");
	int T;
	fin >> T;

	for (int i = 1; i <= T; i++)
	{
		fout << "Case #" << i << ": ";
		int Smax;
		fin >> Smax;

		string in;
		fin >> in;

		int clapped = 0;
		int required = 0;
		for (int i = 0; i <= Smax; i++)
		{
			int k = in[i] - '0';
			while (k--)
			{
				if (i > clapped)
				{
					required += (i - clapped);
					clapped += (i - clapped) + 1;
				}
				else
				{
					clapped++;
				}
			}
		}
		fout << required << "\n";
	}
	//while (1);
	return 0;
}

