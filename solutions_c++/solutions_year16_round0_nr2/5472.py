#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	int t;
	ifstream input("input.in");
	input >> t;
	ofstream output;
	output.open("output.txt");
	for (int i = 0; i < t; ++i) {
		string inp;
		vector<int> b;
		input >> inp;
		int counter = 0;
		for (int j = 1; j < inp.length(); ++j) {
			if ((inp[j] == '+') != (inp[j - 1] == '+')) {
				++counter;
			}
		}
		if (inp[inp.length() - 1] == '-')
			++counter;
		output << "Case #" << i + 1 << ": " << counter << "\n";
	}
}
