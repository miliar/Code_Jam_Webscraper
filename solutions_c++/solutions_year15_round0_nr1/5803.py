#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

#define OUTPUT_PREFIX "Case #"
#define INPUT_NAME "A-large.in"
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
		int callFriend=0,standing=0;
		int sMax;

		input >> sMax;
		string cNum;
		input >> cNum;
		for(int i=0;i<=sMax;i++) {
			int num;
			num=(cNum.at(i)-'0');

			if(i>standing) {
				callFriend+=(i-standing);
				standing=i;
			}
			standing+=num;
		}
		output << OUTPUT_PREFIX << test+1 << ": " << callFriend << endl;
	}
	return 0;
}