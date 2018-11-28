#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t;
	fstream input, output;
	input.open("input.txt", ios::in);
	output.open("output.txt", ios::out);
	input >> t;
	for (int i = 0; i < t; i++) {
		int k, c, s;
		input >> k >> c >> s;
		output << "Case #" << i + 1 << ":";
		for (int j = 0; j < k; j++) {
			output << " " << j+1;
		}
		output << endl;
	}
}

