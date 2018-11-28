#include <fstream>
#include <string>
#include <iostream>
#include <bitset>

using namespace std;

int main() {
	ifstream in("C:/workplace/workspace/code-jam/tmp/A-large.in");
	ofstream out("C:/workplace/workspace/code-jam/tmp/A-large.out");

	int numTestCases;
	in >> numTestCases;

	for (int testCase = 1; testCase <= numTestCases; testCase++) {
		unsigned long n;
		in >> n;

		if (n != 0) {
			unsigned long lastNumber = 0;
			bitset<10> seen;

			while (!seen.all()) {
				lastNumber += n;
				for (unsigned long leftOver = lastNumber; leftOver > 0; leftOver = leftOver / 10) {
					seen.set(leftOver % 10);
				}
			}

			out << "Case #" << testCase << ": " << lastNumber << endl;
		} else {
			out << "Case #" << testCase << ": INSOMNIA" << endl;
		}

	}

	return 0;
}