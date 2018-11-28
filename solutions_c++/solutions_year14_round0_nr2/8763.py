// codejam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	int num;
	fstream fin, fout;

	fin.open("B-large.in");
	fout.open("B-large.out.txt", ios::out);

	fin>>num;

	for(int i = 0; i<num; i++)
	{
		double C, F, X;
		double t = 0, rate = 2.0;
		double t1, tp, tr;

		fin>>C>>F>>X;
		do
		{
			t1 = X / rate;
			tp = C / rate;
			rate += F;
			tr = X / rate;
			
			if (t1 > tp + tr)
				t += tp;	// rate-up
			else
			{
				t += t1;
				break;		// finishing
			}
		} while (1);
		fout.precision(10);

		char szResult[128];
		sprintf_s(szResult, "Case #%d: %.7lf", i+1, t);
		fout<<szResult<<endl;
	}

	fin.close();
	fout.close();
}

