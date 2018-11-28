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
			inputs.cases.push_back(vector<int>(istream_iterator<int>(is), istream_iterator<int>()));
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

	int n;

	for (int i = 0; i < input1.testcases; i++) {
		n = input1.cases[i + 1][0];
		int digitFlags [] = { 1,1,1,1,1,1,1,1,1,1 };
		int tmp = 0;
		int tmptmp = 0;
		int j = 1;
		bool allDigits = false;

		if (n == 0) {
			outfile << "Case #" << (i + 1) << ": INSOMNIA\n";
		}
		else {
			while (!allDigits) {
				tmp = j * n;
				//cout << "got here w: " << tmp << "\n";
				tmptmp = tmp;
				int nDigits[6];
				int k = 0;
				int sum = 0;

				while (tmptmp > 0) {
					nDigits[k] = tmptmp % 10;
					tmptmp = tmptmp / 10;
					digitFlags[nDigits[k]] = 0;
					k++;
					//cout << "tmptmp: " << tmptmp << " k: " << k << "\n";
				}

				bool tmpFlag = true;

				for (int m = 0; m < (sizeof(digitFlags) / sizeof(int)); m++) {
						if (digitFlags[m] == 1) {
							tmpFlag = false;
						}
				}

				allDigits = tmpFlag;

				j++;
			}

			outfile << "Case #" << (i + 1) << ": " << tmp << "\n";
		}
	}

	//
	////

	outfile.close();

	return 0;
}