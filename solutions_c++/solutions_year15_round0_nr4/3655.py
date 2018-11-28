// GoogleCodeJam2015.cpp : Defines the entry point for the console application.

/********   All Required Header Files ********/
#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{	
	ofstream out;
	ifstream in;
	out.open("out.txt");
	in.open("in.txt");
	int t, x, r, c;
	in >> t;

	for (int i = 1; i <= t; i++) {
		in >> x >> r >> c;

		if (x == 1) {
			out << "Case #" << i << ": " << "GABRIEL" << endl;
		}
		else if ((r*c)%x == 0 && r*c >= x*(x - 1)) {
			out << "Case #" << i << ": " << "GABRIEL" << endl;
		}
		else {
			out << "Case #" << i << ": " << "RICHARD" << endl;
		}
	}

	out.close();



	return 0;
}

