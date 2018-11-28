#include <cassert>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>


using namespace std;

int solve(int E, int R, std::vector<int> values)
{
	std::vector<int> s1(E+1,0), s2(E+1,0);
	std::vector<int> *s = &s1, *r = &s2;

	R = min(E,R);

	for (int v : values) {
		for (int e = R ; e <= E ; e++) {
			for (int i = max(R + R - e, 0) ; i <= E + R - e ; i++) {
				(*r)[e] = max((*r)[e], (*s)[e-R+i] + i*v);
			}
		}

		if (s == &s1) {
			s = &s2;
			r = &s1;
		}
		else {
			s = &s1;
			r = &s2;
		}
	}

	return (*s)[R];
}

void read_and_solve(istream &input, ostream &output)
{
	int T;
	input >> T;

	for (int t = 0 ; t < T ; t++) {
		int E, R, N;
		input >> E >> R >> N;

		std::vector<int> values(N);
		for (int &v : values) {
			input >> v;
		}

		output << "Case #" << (t+1) << ": " << solve (E, R, values) << endl;
	}
}


int main(int argc, char **argv) {
	if (argc < 2) {
		cerr << "Not enough parameters" << endl;
		return 1;
	}

	std::string input_file(argv[1]);
	ifstream input(input_file);
	if (!input.is_open()) {
		cerr << "Can't open file " << input_file << endl;
		return 1;
	}

	std::string output_file = input_file.substr(0, input_file.rfind('.')) + ".out";
	ofstream output(output_file, ios::out | ios::trunc);
	if (!output.is_open()) {
		cerr << "Can't open file " << output_file << endl;
		return 1;
	}

	read_and_solve(input, output);

	return 0;
}
