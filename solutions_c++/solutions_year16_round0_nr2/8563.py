// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int t;
	ifstream ifile;
	ofstream ofile;
	ifile.open("B-large.in");
	ofile.open("ans.txt");
	ifile >> t;

	for (int i = 1; i <= t; i++)
	{
		string s;
		ifile >> s;
		int count = 1;
		for (int ii = 1; ii < s.size(); ii++)
		{
			if (s[ii] != s[ii - 1])
				count++;
		}
		if (s[s.size() - 1] == '+')
			count--;
		ofile << "Case #" << i << ": " << count << endl;
	}
    return 0;
}

