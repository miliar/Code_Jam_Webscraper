// codejam.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"

#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>

#define INPUTFILE "B-large.in"
#define OUTPUTFILE "result.out"


using namespace std;

//#pragma warning(disable:4996)


int main()
{
	fstream infile(INPUTFILE,ios::in);
	fstream outfile(OUTPUTFILE,ios::out);
	double C, F, X;
	int caseN, count, i;
	infile >> caseN;
	count = 1;
	double second, produce;
	while (count<=caseN)
	{
		infile >> C >> F >> X;
		second = 0;
		produce = 2;
		while (true){
			if (X / produce < C / produce + X / (produce + F)){
				second += X / produce;
				outfile << "Case #" << count++ << ": " << setiosflags(ios::fixed) << setprecision(7) << second << endl;
				break;
			}
			second += C / produce;
			produce += F;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}

