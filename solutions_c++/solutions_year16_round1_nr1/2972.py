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

bool is_prime(unsigned long long int n) {
	static vector<bool> val;
	if (n + 1 > val.size()) {
		unsigned long long int N = n + 1;
		val.assign(N, true);
		val[0] = false;
		val[1] = false;
		for (unsigned long long int ii = 2; ii * ii < N; ii++) {
			if (!val[ii]) continue;
			for (unsigned long long int jj = ii; ii * jj < N; jj++) {
				val[ii*jj] = false;
			}
		}
	}
	return val[n];
}

template<typename T>
T gcd(T m, T n) {
	if (m == 0) return 0;
	if (n == 0) return 0;
	while (m != n){
		if (m > n) { m = m - n; }
		else       { n = n - m; }
	}
	return m;
}

template<typename T>
T lcm(T m, T n){
	if (m == 0) return 0;
	if (n == 0) return 0;
	return ((m / gcd(m, n)) * n);
}

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		string S;

		ifs >> S;

		reverse(S.begin(), S.end());

		list<char> O;

		O.push_front(S.back());
		S.pop_back();

		while (S.size() > 0) {
			if (O.front() <= S.back()) {
				O.push_front(S.back());
			}
			else {
				O.push_back(S.back());
			}
			S.pop_back();
		}

		for (auto& c : O) {
			ofs << c;
		}
		ofs << endl;
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
