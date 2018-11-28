#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <string>
#include <math.h>
using namespace std;

//Object containing all inputs
class gcjInputs {
	public:
		int testcases;
		//2D jagged vector for all data after the first line.
		vector<vector<int>> cases;
};

gcjInputs getInputs(gcjInputs inputs) {
	ifstream infile("a.in");

	if (infile.is_open()) {
		//First line of input is the test case count.
		infile >> inputs.testcases;

		string oneline;

		//Creates 2D jagged vector for all data after the first line.
		while (getline(infile, oneline)) {
			istringstream is(oneline);
			inputs.cases.push_back(vector<int>(istream_iterator<int>(is),istream_iterator<int>()));
		}
	}
	else {
		cout << "Where's the file dude.";
	}

	infile.close();

	return inputs;
}

int main() {
	gcjInputs input1 = getInputs(input1);
	ofstream outfile;
	outfile.open("output.txt");

	//Start coding here!
	//

	vector<vector<vector<int>>> previous;

	for (int i = 0; i < input1.testcases; i++) {
		int k = input1.cases[i+1][0];
		int c = input1.cases[i+1][1];
		int s = input1.cases[i+1][2];
		long long tmp;

		outfile << "Case #" << (i + 1) << ":";

		for (int j = 1; j <= k; j++) {
			outfile << " " << j;
		}
		outfile << "\n";
	}

	//
	////

	outfile.close();

	return 0;
}