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
		int N;
		ifs >> N;
		int sum = 0;
		vector<pair<string, int>> P(N);
		for (int ii = 0; ii < N; ii++) {
			int tmp;
			ifs >> tmp;
			P[ii].first = 'A' + ii;
			P[ii].second =  tmp;
			sum += tmp;
		}

		while (sum > 0) {
			sort(P.begin(), P.end(), [](pair<string, int>& a, pair<string, int>&b) {return a.second > b.second;});

			if (N == 2) {
				if (sum - 2 >= (P[1].second - 1) * 2) {
					ofs << " " << P[0].first << P[1].first;
					P[0].second--;
					P[1].second--;
					sum -= 2;
				}
				else {
					ofs << " " << P[0].first;
					P[0].second--;
					sum--;
				}

			}
			else {
				if ((sum - 2 >= (P[1].second - 1) * 2) && (sum - 2 >= P[2].second * 2)) {
					ofs << " " << P[0].first << P[1].first;
					P[0].second--;
					P[1].second--;
					sum -= 2;
				}
				else {
					ofs << " " << P[0].first;
					P[0].second--;
					sum--;
				}
			}
		}
		ofs << endl;

		//for (auto& val : P) {
		//	cout << val.first << " " << val.second << endl;
		//}
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
		ofs << "Case #" << No << ":";
		cout << "Case #" << No << "...";
		Solver(ifs, ofs);
		cout << endl;
	}
}
