#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <string>
#include <math.h>
#include <deque>
using namespace std;

//Object containing all inputs
class gcjInputs {
public:
	int testcases;
	//2D jagged vector for all data after the first line.
	vector<vector<char>> cases;
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
			inputs.cases.push_back(vector<char>(istream_iterator<char>(is), istream_iterator<char>()));
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

	for (int i = 1; i <= input1.testcases; i++) {
		deque<char> tmp;

		tmp.push_back(input1.cases[i][0]);
		for (int j = 1; j < input1.cases[i].size(); j++) {

			if (input1.cases[i][j] >= tmp.front()) {
				tmp.push_front(input1.cases[i][j]);
			}
			else {
				tmp.push_back(input1.cases[i][j]);
			}
		}

		outfile << "Case #" << i << ": ";

		for (int j = 0; j < tmp.size(); j++) {
			outfile << tmp[j];
		}

		outfile << "\n";
	}

	//
	////

	outfile.close();

	return 0;
}