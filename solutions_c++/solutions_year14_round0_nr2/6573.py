// Qual 1B Cookie Clicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in;
	ofstream out;

	int T;
	double C,F,X;

	in.open(argv[1]);
	out.open("output.txt");

	in >> T;

	for(int i=1;i<=T;++i) {
		in >> C >> F >> X;
		int n=0;
		double base=X/(F*n+2.0);
		double min=base;
		n++;
		double cur=X/(F+2.0)+C/2;
		base=X/(F*n+2.0);
		while(cur<min) {
			min=cur;
			cur-=base;
			cur+=C/(F*n+2.0);
			n++;
			base=X/(F*n+2.0);
			cur+=base;
		}

		out << fixed << setprecision(7) << "Case #" << i << ": " << min << endl;
	}

	return 0;
}

