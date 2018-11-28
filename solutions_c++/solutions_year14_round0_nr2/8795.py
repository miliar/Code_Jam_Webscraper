//============================================================================
// Name        : gcj2014.cpp
// Author      : rajappan
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <cmath>
using namespace std;

#define EPS 1e-6

bool equal(double a, double b) {
	return fabs(a - b) < EPS;
}

bool comp(double a, double b) {
	return a < b;
}

int main() {
	int T;
	ifstream infile(
			"/home/grad06/rajappan/workspace/gcj2014/src/B-large.in");
	ofstream outfile(
			"/home/grad06/rajappan/workspace/gcj2014/src/B-large.out");
	if (!infile) {
		cout << "Error opening file!" << endl;
		exit(1);
	}
	infile >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		double C, F, X, curF = 2.0, ans = 0.;
		infile >> C >> F >> X;

		cout << "Case #" << caseNum << ": ";
		outfile << "Case #" << caseNum << ": ";

		cout.unsetf(std::ios::floatfield);
		cout.precision(7);

		outfile.unsetf(std::ios::floatfield);
		outfile.precision(7);

		if (comp(X / curF, C / curF)) {
			cout << X / curF << endl;
			outfile << X / curF << endl;
			continue;
		}
		while (comp(C / curF + X / (curF + F), X / curF)) {
			// buy farm
			ans += C / curF;
			curF += F;
		}
		ans += X / curF;

		cout << ans << endl;
		cout.setf(std::ios::fixed, std::ios::floatfield);

		outfile << ans << endl;
		outfile.setf(std::ios::fixed, std::ios::floatfield);
	}
	infile.close();
	outfile.close();
	return 0;
}
