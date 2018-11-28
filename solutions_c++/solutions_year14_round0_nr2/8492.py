#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <limits>
#include <iomanip>

using namespace std;

int main() {

	int testCase;

	double C,F,X;

	double result;
	double bolen=2;

	ifstream input;
	input.open("test.inp");
	ofstream output("test.out");
	input >> testCase;
	for (int i=0; i<testCase; i++) {

		input >> C >> F >> X;
		result=0;
		bolen=2;

		while((X/(bolen+F))<((X-C)/bolen)) {
			result += C/bolen;
			bolen+=F;
		}

		result += (X/bolen);
		output << "Case #" << i+1 << ": " <<  setiosflags( ios::fixed ) << std::setprecision(7) << (double)result << endl;
	}

	
	return 0;
}
