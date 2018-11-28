#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <string>
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
			inputs.cases.push_back(vector<char>(istream_iterator<char>(is),istream_iterator<char>()));
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

	for (int i = 0; i < input1.testcases; i++) {
		int flips = 0;
		if (input1.cases.at(i + 1).at(input1.cases.at(i + 1).size() - 1) == '-') {
			flips++;
		}

		if (input1.cases.at(i + 1).size() > 1) {
			for (int j = input1.cases.at(i + 1).size() - 1; j > 0; j--) {
				if (input1.cases.at(i + 1).at(j) == '+') {
					if (input1.cases.at(i + 1).at(j - 1) == '-') {
						flips++;
					}
				}
				else {
					if (input1.cases.at(i + 1).at(j - 1) == '+') {
						flips++;
					}
				}

			}
		}

		outfile << "Case #" << (i+1) << ": " << flips << "\n";
	}

	//
	////

	outfile.close();

	return 0;
}