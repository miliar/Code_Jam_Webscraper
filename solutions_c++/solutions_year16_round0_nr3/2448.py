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

int convBase(int a, int b) {
	int result = 0;

	return result;
}

int main() {
	//gcjInputs input1 = getInputs(input1);
	ofstream outfile;
	outfile.open("output.txt");

	//Start coding here!
	//

	outfile << "Case #1:\n";

	int n = 16;
	int j = 50;
	int jcount = 0;
	long long jamcoin = pow(2, n - 1) + 1; //n bits, i.e. n=6 => {1,0,0,0,0,1}
	int divisors[9] = { 0,0,0,0,0,0,0,0,0 }; //Capture divisors
	
	//Each iteration creates a jamcoin
	while ((jcount < j) && (jamcoin < pow(2, (n)))) {
		//cout << jamcoin << " ";
		bool notPrime = false; //Default to prime
		int goodJamcoin = 0; //Counts to 10 good divisors
		//Each iteration creates a baseset
		long long baseSet[9] = { 0,0,0,0,0,0,0,0,0 }; //Base 2 through 10
		for (int k = 1; k <= sizeof(baseSet) / sizeof(long long); k++) {
			//Each iteration runs through the jamcoin bitfield for one baseset element
			long long tmp = jamcoin;
			for (int l = 0; l < log(jamcoin) / log(2); l++) {
				int curBit = (int)((tmp >> l) % 2);
				baseSet[k - 1] += curBit * pow(k + 1, l);
			}

			//Checks the baseset element for prime
			for (long m = 2; m <= sqrt(baseSet[k - 1]); m++) {
				if ((baseSet[k - 1] % m) == 0) {
					notPrime = true;
					//If not prime, record divisor and mark as valid jamcoin and skip rest of test
					divisors[k - 1] = m;
					goodJamcoin += 1;
					break;
				}
			}
			//cout << baseSet[k - 1] << " ";
		}
		//cout << "\n";
		if (goodJamcoin == 9) {
			outfile << baseSet[8] << " ";
			//cout << baseSet[8] << "\n";
			for (int o = 0; o < sizeof(divisors) / sizeof(int); o++) {
				outfile << divisors[o] << " ";
			}
			outfile << "\n";
			jcount++;
		}

		//Generate next jamcoin attempt
		jamcoin +=2;
	}

	//
	////

	outfile.close();

	return 0;
}