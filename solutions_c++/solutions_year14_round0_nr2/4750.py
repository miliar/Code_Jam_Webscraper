// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
 
using namespace std;

std::ifstream infile("E:\\maye\\test 2\\Debug\\in.txt");
std::ofstream outfile("E:\\maye\\test 2\\Debug\\out.txt");

int T;

void doit()
{
	infile >> T;
	cout << "T = " << T << endl;
	double delta = 1e-8;
	for (int i = 0; i < T; ++i)
	{
		double C, F, X;
		double time = 0.0; 
		double f = 2.0;

		infile >> C >> F >> X;

 
		while (X > delta)
		{ 
			if (X - C < delta)
			{
				time += X / f;
				break;
			}
			else if (X / f - (C/ f + X / (f + F)) < delta)
			{
				time += X / f;
				break;
			}
			else 
			{
				time += C / f; 
				f += F;
			} 
		}

		outfile << "Case #" << i + 1 << ": ";
		outfile << std::setprecision(7) << fixed<< time << endl;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	doit();
	return 0;
}

