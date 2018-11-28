#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
	ifstream input;
	input.open("input.in");
	ofstream output;
	output.open("output.in");
	int t;
	input >> t;

	for (int i = 0; i < t; ++i) {
		string line;
		input >> line;
		char current = line[0];
		int answer = 0;
		for (int i = 0; i < line.size(); ++i) {
			if (line[i] != current) {
				answer++;
				current = line[i];
			}
		}
		if (current == '-') { answer++; }
		output << "Case #" << i + 1 << ": " << answer << endl;
	}
	input.close();
	output.close();
	return 0;
}