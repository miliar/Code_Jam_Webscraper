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

	int X = 0;
	int R = 0;
	int C = 0;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		infile >> X;
		infile >> R;
		infile >> C;

		if(X < 7
			&& R*C%X == 0
			&& (R>=X-1) && (C>=X-1))
		{

			outfile << "GABRIEL" << endl;
			cout << "GABRIEL" << endl;
		}
		else
		{
			outfile << "RICHARD" << endl;
			cout << "RICHARD" << endl;
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

		//outfile << endl;

	}

	return 0;
}
