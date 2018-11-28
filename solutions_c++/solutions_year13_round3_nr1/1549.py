#include <cassert>
#include <cmath>
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
		string v;
		int n;
		in >> v >> n;
		int m = v.size();
		int consonants = 0, count = 0, distance = m;

		for (int i = 0 ; i < m ; i ++) {
			char c = v[i];
			if (c == 'a' || c == 'e' || c == 'i' || c == 'o'|| c == 'u')
				consonants = 0;
			else
				consonants ++;

			if (consonants >= n)
				distance = 0;

			count += max(0, i+2 - distance - n);
			distance ++;
		}


		out << "Case #" << (t+1) << ": " << count << endl;
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
