#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	string name = "C-large.in";
	ifstream input;
	input.open(name);
	ofstream output("out_" + name);
	int T;
	input >> T >> ws;
	for (int cases = 1; cases <= T; cases++) {
		output << "Case #" << cases << ":" << endl;
		int N, J;
		input >> N >> J;
		int bits = 0;
		for (int i = 0; i < J; i++) {
			output << 11;
			for (int j = 0; j < (N - 4)/2; j++) {
				if (bits & (1 << j))
					output << "11";
				else
					output << "00";
			}
			output << "11 3 2 5 2 7 2 9 2 11"<<endl;
			bits++;
		}
	}
	return 0;
}