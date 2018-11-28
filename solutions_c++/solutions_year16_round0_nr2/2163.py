#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main() {
	string name = "B-large.in";
	ifstream input;
	input.open(name);
	ofstream output("out_" + name);
	int T;
	input >> T >> ws;
	for (int cases = 1; cases <= T; cases++) {
		output << "Case #" << cases << ": ";
		string line;
		getline(input, line);
		istringstream iss(line);
		char lastpan;
		iss >> lastpan;
		int count = 0;
		char pan;
		while (iss >> pan) {
			if (pan != lastpan)
				count++;
			lastpan = pan;
		}
		if (lastpan == '-')
			count++;
		output << count << endl;
	}
	return 0;
}