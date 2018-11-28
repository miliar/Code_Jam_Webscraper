#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream in(argv[1]);

	string out_file = argv[1];
	out_file = out_file.substr(0, out_file.size()-2) + "out";
	ofstream out(out_file);

	int T; // TEST CASES
	in >> T;

	for(int i = 1; i <= T; ++i) {
		int Smax;
		in >> Smax;

		string str;
		in >> str;

		int invite = 0;
		int already_up = stoi(str.substr(0, 1));

		for(int s = 1; s <= Smax; ++s) {
			int current_row = stoi(str.substr(s, 1));
			if (current_row == 0) continue;

			if (already_up < s) {
				invite += (s - already_up);
				already_up += invite;
			}

			already_up += current_row;

			if (already_up >= Smax) break;
		}
		out << "Case #" << i << ": " << invite << endl;
	}

	return 0;
}