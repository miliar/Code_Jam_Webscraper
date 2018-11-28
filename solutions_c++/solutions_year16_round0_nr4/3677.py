#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int t;
	ifstream input("input.in");
	input >> t;
	ofstream output;
	output.open("output.txt");
	for (int i = 0; i < t; ++i) {
		int k, s, c;
		input >> k;
		input >> s;
		input >> c;
		output << "Case #" << i + 1 << ": ";
		for (int j = 0; j < k; ++j) {
			output << j + 1 << " ";
		}
		output << "\n";
	}
}
