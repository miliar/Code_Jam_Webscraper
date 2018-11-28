#include <algorithm>
#include <fstream>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace std;

string solve(string& input)
{
	int numFlips = 0;
	for (;;) {
		auto last = input.find('-');
		if (last == string::npos) {
			return to_string(numFlips);
		}
		if (last == 0) {
			last = input.find('+');
			if (last == string::npos) {
				last = input.size();
			}
		}
		reverse(&input[0], &input[last]);
		for_each(&input[0], &input[last], [](char& ch){ ch = '+' + '-' - ch; });
		++numFlips;
	}
}

int main(int argc, char *argv[])
{
	unique_ptr<ifstream> in_p;
	if (argc > 1) {
		in_p.reset(new ifstream(argv[1]));
		cin.rdbuf(in_p->rdbuf());
	}
	int numCases;
	cin >> numCases;
	cin.ignore();
	vector<string> input(numCases);
	vector<string> output(numCases);
	for (int i = 0; i < numCases; ++i) {
		cin >> input[i];
		cin.ignore();
	}
	#pragma omp parallel for
	for (int i = 0; i < numCases; ++i) {
		output[i] = solve(input[i]);
	}
	for (int i = 0; i < numCases; ++i) {
		cout << "Case #" << i + 1 << ": " << output[i] << endl;
	}
}
