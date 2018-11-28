/**
*	CookieClickerAlpha.cpp
*	Copyright 2014, Matt Parish
*
*	See CookieClickerAlpha.pdf for problem description and sample input/output.
*
*/

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

const string INPUT_FILE = "B-large.in";
const string OUTPUT_FILE = "B-large.out";

int main() {
	ifstream in(INPUT_FILE);
	if(in.fail()) {
		cerr << INPUT_FILE << " failed to open.\n";
		exit(1);
	}

	ofstream out(OUTPUT_FILE);
	if(out.fail()) {
		cerr << OUTPUT_FILE << " failed to open.\n";
		exit(2);
	}
	out << fixed << setprecision(7);

	double c, f, x, p, totalTime=0.0;
	c=f=x=p=0.0;

	int numCases=0;
	in >> numCases;

	for(int currCase=1; currCase<=numCases; ++currCase) {
		in >> c >> f >> x;
		p = 2.0;
		totalTime=0.0;

		// While the time it would take to win is greater than the
		// time it would take to buy another farm and win
		while(x/p > c/p + x/(p+f)) {
			totalTime += c/p;
			p += f;
		}

		totalTime += x/p;

		out << "Case #" << currCase << ": " << totalTime << endl;
	}

	in.close();
	out.close();

	return 0;
}