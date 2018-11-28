#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		string S;
		ifs >> S;
		string::reverse_iterator rit = S.rbegin();
		for (;rit != S.rend(); rit++) {
			if (*rit == '-') break;
		}
		int count = 0;
		char before = '+';
		for (;rit != S.rend(); rit++) {
			if (*rit == before) continue;
			count++;
			before = (before == '+') ? '-' : '+';
		}
		ofs << count << endl;
	}
};

void main(int argc, char* argv[]) {
	string fname_i = argv[1];
	string fname_o = fname_i.substr(0, fname_i.find_last_of(".")) + ".out";
	ifstream ifs(fname_i);
	ofstream ofs(fname_o);

	int T;
	ifs >> T;
	for (int No = 1; No <= T; No++) {
		ofs << "Case #" << No << ": ";
		cout << "Case #" << No << "...";
		Solver(ifs, ofs);
		cout << endl;
	}
}
