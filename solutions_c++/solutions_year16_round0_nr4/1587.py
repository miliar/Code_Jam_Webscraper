#include <fstream>
#include <iostream>
using namespace std;
int main() {
	ifstream input;
	input.open("input.in");
	ofstream output;
	output.open("output.in");
	int t;
	input >> t;
	for (int i = 0; i < t; ++i) {
		int a, b, c;
		input >> a >> b >> c;
		output << "Case #" << i + 1 << ":";
		for (int i = 0; i < a; ++i) {
			output << " " << i + 1;
		}
		output << endl;
	}
	input.close();
	output.close();
	return 0;
}