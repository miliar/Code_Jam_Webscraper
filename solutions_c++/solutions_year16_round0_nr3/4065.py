#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <string>
#include <bitset>

using namespace std;

long long int gcd(long long int m, long long int n) {
	if ((0 == m) || (0 == n)) return 0;
	while (m != n) {
		if (m > n) {
			m -= n;
		}
		else {
			n -= m;
		}
	}
	return m;
}

long long int lcm(long long int m, long long int n) {
	return ((0 == m) || (0 == n)) ? 0 : ((m / gcd(m, n)) * n);
}

unsigned long long int get_non_prime(unsigned long long int val) {
	if (val % 2 == 0) return 2;
	for (unsigned long long int ii = 3; ii <= val / ii; ii += 2) {
		if (val % ii == 0) return ii;
	}
	return 0;
}

class Solver {

public:
	Solver(ifstream& ifs, ofstream& ofs) {
		unsigned long long int N;
		unsigned long long int J;
		ifs >> N;
		ifs >> J;

		unsigned long long int s = pow(2, N-1);
		s += 1;

		unsigned long long int e = 0;
		for (int ii = 0; ii < N; ii++) {
			e += pow(2, ii);
		}

		ofs << endl;
		vector<unsigned long long int> bases(11);
		vector<unsigned long long int> result(11);
		unsigned long long int count = 0;
		for (unsigned long long int cur = s; cur <= e; cur+=2) {
			bool flg = true;
			for (unsigned long long int base = 2; base <= 10; base++) {
				unsigned long long int tmp = cur;
				unsigned long long int sum = 0;
				for (unsigned long long int n = 0; n < N; n++) {
					sum += (tmp & 1) * pow(base, n);
					tmp >>= 1;
				}
				bases[base] = sum;
				result[base] = get_non_prime(sum);
				if (result[base] == 0 && result[base] != cur) {
					flg = false;
					break;
				}
			}
			if (flg) {
				stringstream ss;
				ss << static_cast<std::bitset<32>>(cur);

				// debug
				for (unsigned long long int base = 2; base <= 10; base++) {
					cout << "base(" << base << "):" << bases[base] << endl;
				}
				cout << ss.str().substr(32-N, N);
				for (unsigned long long int base = 2; base <= 10; base++) {
					cout << " " << result[base];
				}
				cout << endl;

				// output
				ofs << ss.str().substr(32 - N, N);
				for (unsigned long long int base = 2; base <= 10; base++) {
					ofs << " " << result[base];
				}
				ofs << endl;

				count++;
				if (count == J) break;
			}
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
		ofs << "Case #" << No << ":";
		cout << "Case #" << No << "...";
		Solver(ifs, ofs);
		cout << endl;
	}
}
