#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>

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
		
		map<char, int> S;
		char temp;
		while (iss >> temp) {
			S[temp]++;
		}
		vector<int> number(10, 0);

		number[0] += S['Z'];
		S['E'] -= S['Z'];
		S['R'] -= S['Z'];
		S['O'] -= S['Z'];
		S['Z'] -= S['Z'];

		number[2] += S['W'];
		S['T'] -= S['W'];
		S['O'] -= S['W'];
		S['W'] -= S['W'];

		number[4] += S['U'];
		S['F'] -= S['U'];
		S['O'] -= S['U'];
		S['R'] -= S['U'];
		S['U'] -= S['U'];

		number[5] += S['F'];
		S['I'] -= S['F'];
		S['V'] -= S['F'];
		S['E'] -= S['F'];
		S['F'] -= S['F'];

		number[6] += S['X'];
		S['S'] -= S['X'];
		S['I'] -= S['X'];
		S['X'] -= S['X'];

		number[7] += S['V'];
		S['S'] -= S['V'];
		S['E'] -= 2 * S['V'];
		S['N'] -= S['V'];
		S['V'] -= S['V'];

		number[8] += S['G'];
		S['E'] -= S['G'];
		S['I'] -= S['G'];
		S['H'] -= S['G'];
		S['T'] -= S['G'];
		S['G'] -= S['G'];

		number[9] += S['I'];
		number[1] += S['O'];
		number[3] += S['R'];

		for (int i = 0; i < 10; i++)
		{
			while (number[i]) {
				output << i;
				number[i]--;
			}
		}

		output << endl;
	}
	output.close();
	input.close();
	return 0;
}