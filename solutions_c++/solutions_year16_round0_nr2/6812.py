// revenge.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("data.in");
	ofstream fout("data.out");
	int t;
	fin >> t;
	int c;
	for (c = 1; c <= t; c++)
	{
		string s;
		fin >> s;
		string::iterator it;
		int a[500];
		if (*s.begin() == '-') a[0] = 1;
		else a[0] = 0;
		int i = 0;
		for (it = s.begin()+1; it != s.end(); it++)
		{
			i++;
			if (*(it - 1) == '+' && *it == '-')
			{
				a[i] = a[i - 1] + 2;
			}
			else a[i] = a[i - 1];
		}
		fout << "Case #" << c << ": " << a[i] << '\n';
	}
	return 0;
}

