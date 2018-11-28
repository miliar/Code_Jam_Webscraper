// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	std::ifstream fin("in.txt");
	std::ofstream fout("out.txt");

	long long T;
	string str;

	fin >> T;

	for (int t = 1; t <= T; ++t) {

		fin >> str;

		long long len = str.length();
		long long sol = str[len-1] == '-' ? 1 : 0;

		long long i = 1;
		while ( i < len )
		{
			if (str[i] != str[i - 1]) {
				sol++;
			}
			++i;
		}

		fout << "Case #" << t << ": " << sol << endl;

	}


    return 0;
}

