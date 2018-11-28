#include <cassert>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>

// #include <gmpxx.h>


using namespace std;



void read_and_solve(istream &in, ostream &out)
{
	int T;
	in >> T;

	for (int t = 0 ; t < T ; t++) {
		int A, N;
		in >> A;
		in >> N;

		vector<int> motes(N);
		for (int &m : motes) {
			in >> m;
		}

		sort(motes.begin(), motes.end());

		int r = N, a = A, eat = 0, remaining = N;

		for (int &m : motes) {
			if ((a <= 1 && m > 0) || a <= 0)
				break;

			while (a <= m) {
				a = 2 *a - 1;
				eat++;
			}
			a += m;
			remaining--;
			r = min(r, remaining + eat);
		}

		out << "Case #" << (t+1) << ": " << r << endl;

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
