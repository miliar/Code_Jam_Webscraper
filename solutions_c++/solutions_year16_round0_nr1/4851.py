#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		vector<bool> check;
		check.assign(10, false);
		long long int start;
		int true_num = 0;

		ifs >> start;

		if (start == 0) {
			ofs << "INSOMNIA" << endl;
			return;
		}

		long long int sum = start;
		while (true_num < 10) {
			long long int cur = sum;
			while (cur >= 1) {
				int a = cur % 10;
				cur = cur / 10;
				if (check[a]) {
					continue;
				}
				check[a] = true;
				true_num++;
				if (true_num == 10) {
					ofs << sum << endl;
					return;
				}
			}
			sum += start;
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
