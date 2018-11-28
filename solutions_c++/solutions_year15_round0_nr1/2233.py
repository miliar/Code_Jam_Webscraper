#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");

	int T;
	input >> T;
	for (int i = 0; i < T; ++i) {
		int top;
		string levels;
		input >> top >> levels;
		int standing = 0;
		int friends = 0;
		for (int j = 0; j <= top; ++j) {
			int num = levels[j] - '0';
			if (num > 0) {
				if (standing < j) {
					friends += j - standing;
					standing = j;
				}
				standing += num;
			}
		}
		output << "Case #" << (i + 1) << ": " << friends << endl;
	}

	return 0;
}