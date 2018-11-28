#include <fstream>
#include <string>
#include <iostream>
#include <bitset>

using namespace std;

int main() {
	ifstream in("C:/workplace/workspace/code-jam/tmp/B-large.in");
	ofstream out("C:/workplace/workspace/code-jam/tmp/B-large.out");

	int numTestCases;
	in >> numTestCases;

	for (int testCase = 1; testCase <= numTestCases; testCase++) {
		string line;
		in >> line;
		
		int numFlips = 0;
		char lastSign = line[0];
		for (string::iterator it = line.begin(); it < line.end(); it++) {
			if (*it != lastSign) {
				numFlips++;
				lastSign = *it;
			}
		}

		if (lastSign == '-') {
			numFlips++;
		}

		out << "Case #" << testCase << ": " << numFlips << endl;
	}

	return 0;
}