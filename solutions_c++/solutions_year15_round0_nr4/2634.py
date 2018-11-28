#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

#define OUTPUT_PREFIX "Case #"
#define INPUT_NAME "D-small-attempt4.in"
#define OUTPUT_NAME "output.dat"

using namespace std;

int main() {
	ifstream input;
	ofstream output;

	int testcase;

	input.open(INPUT_NAME);
	output.open(OUTPUT_NAME);

	input >> testcase;

	for(int test=0;test<testcase;test++) {
		int X,R,C;

		input >> X >> R >> C;
		int min = X/2;

		if(X>=7) {
			output << OUTPUT_PREFIX << test+1 << ": " << "RICHARD" << endl;
		} else if(X>=3&&(min>=R||min>=C)) {
			output << OUTPUT_PREFIX << test+1 << ": " << "RICHARD" << endl;
		} else if((R*C)%X) {
			output << OUTPUT_PREFIX << test+1 << ": " << "RICHARD" << endl;
		} else {
			output << OUTPUT_PREFIX << test+1 << ": " << "GABRIEL" << endl;
		}
	}
	return 0;
}