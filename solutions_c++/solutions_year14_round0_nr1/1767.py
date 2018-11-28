//=====================7=======================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

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
	int a1 = 0;
	int a2 = 0;

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		infile >> a1;

		cout << a1 << endl;


		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				infile >> d1[i][j];
			}
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

		infile >> a2;
		cout << a2 << endl;

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				infile >> d2[i][j];
			}
		}

		int ansNum=0;
		int ans =0;

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(d2[a2-1][i] == d1[a1-1][j])
				{
					ansNum++;
					ans = d2[a2-1][i];
				}

			}
		}

		if(ansNum == 1)
		{
			cout << ans << endl;
			outfile << ans << endl;
		}
		else if(ansNum == 0)
		{
			cout << "Volunteer cheated!" << endl;
			outfile << "Volunteer cheated!" << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
			outfile << "Bad magician!" << endl;
		}




		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		//outfile << result << endl;
		//cout << result << endl;
		//outfile << endl;

	}

	return 0;
}
