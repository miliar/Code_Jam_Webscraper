//=====================7=======================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

//#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
#include <iostream>
#include <string>
#include <fstream>
//#include <sstream>
//#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdarg.h>
#include <gmpxx.h>
#include <iomanip>


using namespace std;

int main(int argc, char** argv)
{
	if(argc!=3)
	{
		cout << "Usage:" << endl;
		cout << "jam_test infile outfile" << endl;
		return 0;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	if(!infile)
		cout << "Input file open error!" << endl;

	if(!outfile)
		cout << "Output file open error!" << endl;

	int nCase;

	int i,j;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{

		string str;

		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		infile >> str;

		cout << "str=" << str << endl;

		bool reversed = false;
		char match = '+';
		int ans = 0;

		for(int i=str.length()-1;i>=0; i--)
		{
			if(reversed)
				match = '-';
			else
				match = '+';

			while(i>0 && str[i] == match)
				i--;

			if(i>0)
			{
				ans++;
				reversed = !reversed;
			}
			else
			{
				if(str[i] != match)
					ans++;
			}
		}

		outfile << ans << endl;
		cout << ans << endl;

		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		//outfile << result << endl;
		//cout << result << endl;
		//outfile << endl;

	}

	return 0;
}
