// GCodeJam_CookieClicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
using namespace std;

bool ShouldIBuyFarm(double C, double F, double X, double totalProd, double prod)
{
	double sec1 = (X) / prod;
	double sec2 = C / prod + (X) / (prod + F) ;

	if(sec1 < sec2) {
		// don't buy.
		return false;
	}
	else
		return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int n;

	ifstream inf;
	ofstream outf;
	inf.open("some.txt");
	outf.open("result.txt");
	if(!inf.is_open() || !outf.is_open())
		return 0;

	inf >> n;
	//std::ofstream.setf( std::ios::fixed, std::ios::floatfield ); // floatfield set to fixed

	for(int i = 0 ; i < n ; i++) {
		double C, X, F;
		inf >> C; // farm cost.
		inf >> F; // farm production.
		inf >> X; // goal.
		
		double totalProd = 0.0, prod = 2.0;
		vector<double> seconds;
		bool bAccomplished = false;

		while(!bAccomplished) {

			if(ShouldIBuyFarm(C, F, X, totalProd, prod)) {
				// compute, save history and buy and go on.
				double sec = (C - totalProd) / prod;
				prod += F;
				totalProd = 0.0;
				seconds.push_back(sec);
			}
			else {
				// just compute/sum up the whole history. and return result.
				double sec = (X - totalProd) / prod;
				seconds.push_back(sec);
				double sumTime = 0.0;
				for(size_t i = 0 ; i < seconds.size() ; i++) {
					sumTime += seconds.at(i);
				}
				// print sumTime.

				char tmp[1000];
				sprintf_s(tmp, "%0.10f", sumTime);
				outf << "Case #" << i + 1 << ": " << tmp << endl;
				
				
				bAccomplished = true;
			}

		}


	}


	return 0;
}
