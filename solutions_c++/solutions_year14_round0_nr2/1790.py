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
#include <iomanip>

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

	infile >> nCase ;
	cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{

		double lastTime = 0;
		double currentTime = 0;
		double C, F, X;
		double lostTime = 0;
		int n = 0;
		double speed = 0;

		cout << "Case #" << iCase+1 << ": ";
		outfile << "Case #" << iCase+1 << ": ";

		infile >> C;
		infile >> F;
		infile >> X;

		cout << "C=" << C << endl;
		cout << "F=" << F << endl;
		cout << "X=" << X << endl;

		speed = 2;
		lastTime = X / speed;

		while(currentTime < lastTime)
		{
			n++;
			lastTime = (currentTime==0? lastTime: currentTime);

			lostTime += C / speed;
			speed = 2.0 + F * n;

			currentTime = lostTime + X / speed;
		}

		cout <<  std::fixed << std::setprecision(7) << lastTime << endl;
		outfile <<  std::fixed << std::setprecision(7) << lastTime << endl;

		//cout << "\n    " << r << "\n*\n    " << t;
		//cout << "\n--------------------\n" << r * t << "\n\n";

		//outfile << result << endl;
		//cout << result << endl;
		//outfile << endl;

	}

	return 0;
}
