#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>

#include <vector>
#include <list>
#include <map>
#include <string>
#include <set>

#include <algorithm>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		long long int B;
		long long int M;
		ifs >> B;
		ifs >> M;

		long long int sum = pow(2, B - 2);
		long long int extra = sum - M;

		if (M > sum) {
			ofs << "IMPOSSIBLE" << endl;
		}
		else {
			ofs << "POSSIBLE" << endl;

			// 1->x
			ofs << "0";
			for (int jj = 1; jj < B; jj++) {
				ofs << "1";
			}
			ofs << endl;

			// 2,3..B-1->x
			for (int ii = 1; ii < B - 1; ii++) {
				ofs << "0";
				for (int jj = 1; jj < ii; jj++) {
					ofs << "1";
				}
				for (int jj = ii; jj < B - 1; jj++) {
					ofs << "0";
				}
				if (extra == 0 || extra < pow(2, B - 2 - ii)) {
					ofs << "1";
				}
				else {
					ofs << "0";
					extra -= pow(2, B - 2 - ii);
				}
				ofs << endl;
			}

			// B->x
			for (int jj = 0; jj < B; jj++) {
				ofs << "0";
			}
			ofs << endl;
		}
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
