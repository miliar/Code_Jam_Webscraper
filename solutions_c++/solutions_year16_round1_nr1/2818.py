#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

int main() {
	string file = "A-large.in";
	ifstream input;
	input.open(file);
	ofstream output;
	output.open("out_" + file);
	int T;
	input >> T >> ws;
	for (int cases = 1; cases <= T; cases++)
	{
		output << "Case #" << cases << ": ";
		string line;
		getline(input, line);
		istringstream iss(line);
		vector<char> S;
		char temp;
		while (iss >> temp) {
			S.push_back(temp);
		}
		int length = S.size();
		vector<int> rev;
		while (length) {
			int pos = 0;
			char letter = S[pos];
			for (int i = 0; i < length; i++) {
				if (S[i] >= S[pos]) {
					pos = i;
					letter = S[pos];
				}
			}
			rev.push_back(pos);
			length = pos;
		}

		for (int i = 0; i < rev.size(); i++) {
			output << S[rev[i]];
			S[rev[i]] = '0';
		}
		for (int i = 0; i < S.size(); i++) {
			if (S[i] != '0')
				output << S[i];
		}
		output << endl;
	}
	output.close();
	input.close();
	return 0;
}