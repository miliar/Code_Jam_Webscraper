//=====================7=======================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
//$ clang++ -g a.cpp -o jam_test

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
//#include <sstream>
//#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdarg.h>
#include <gmpxx.h>

using namespace std;

int d1[4][4];
int d2[4][4];

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
	int sMax = 0;
	char c;
	int shy = 0;
	int y =0;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		y = shy = 0;

		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		infile >> sMax;

//		cout << sMax << " ";//endl;


		for(i=0; i<=sMax; i++)
		{
			infile >> c;
			//cout << c << ',';
			c = c - '0'; //to int
			if(i > shy && c != 0)
			{
				y += i - shy;
				shy += y;
			}
			shy += c;
		}

//		for(i=0;i<4;i++)
//		{
//			for(j=0;j<4;j++)
//			{
//				cout << d1[i][j] << " ";
//			}
//
//			cout << endl;
//		}


		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		outfile << y << endl;
		cout << y << endl;
		//outfile << endl;

	}

	return 0;
}
