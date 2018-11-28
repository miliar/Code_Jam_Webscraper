#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <array>
#include <ctime>
#include <random>
#include <iomanip>

using namespace std;
typedef long long ll;

class Term {
	int code;
	bool sign;
public:
	Term(int code_ = 1, bool sign_ = false) : code(code_), sign(sign_) {}
	explicit Term(char c) {
		sign = false;
		if (c == 'i')
			code = 2;
		else if (c == 'j')
			code = 3;
		else
			code = 4;
	}
	Term& operator *=(const Term& r) {
		sign ^= r.sign;
		if (code == 1)
			code = r.code;
		else if (code == 2) {
			switch (r.code) {			
			case 2: code = 1; sign ^= 1; break;
			case 3: code = 4; break;
			case 4: code = 3; sign ^= 1; break;
			}
		}
		else if (code == 3) {
			switch (r.code) {
			case 2: code = 4; sign ^= 1; break;
			case 3: code = 1; sign ^= 1; break;
			case 4: code = 2; break;
			}
		}
		else {
			switch (r.code) {
			case 2: code = 3; break;
			case 3: code = 2; sign ^= 1; break;
			case 4: code = 1; sign ^= 1; break;
			}
		}
		return *this;
	}
	friend const Term operator *(Term a, const Term& b) {
		return a *= b;
	}
	bool operator ==(const Term& r) const {
		return code == r.code && sign == r.sign;
	}
};

bool calc(const string& s) {
	int n = s.size();
	static const Term I = Term('i');
	static const Term J = Term('j');
	static const Term K = Term('k');	
	vector<char> used(n);
	Term left;
	for (int i = 0; i < n; ++i) {
		left *= Term(s[i]);
		if (left == I) {
			Term middle;
			for (int j = i + 1; j + 1 < n; ++j) {
				middle *= Term(s[j]);
				if (middle == J) {					
					if (used[j + 1])
						continue;
					else {
						Term right;
						for (int k = j + 1; k < n; ++k)
							right *= Term(s[k]);
						if (right == K)
							return true;
						used[j + 1] = true;						
					}
				}
			}
		}
	}
	return false;
}


void solve() {
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	auto beg = clock();	
	fin >> t;
	for (int q = 0; q < t; ++q) {
		int l, x;
		string tmp;
		fin >> l >> x >>tmp;
		string s;
		for (int i = 0; i < x; ++i)
			s += tmp;
		fout << "Case #" << q + 1 << ": ";
		fout << (calc(s) ? "YES\n" : "NO\n");
		cout << "Case #" << q + 1 << "\n";
	}
	cout << "Done for " << (clock() - beg) * 1.0 / CLOCKS_PER_SEC;
}

void test() {
	default_random_engine gen(5748548);
	uniform_int_distribution<int> dist('a', 'z');
	auto beg = clock();
	for (int q = 1; q <= 100; ++q) {
		string s;
		for (int i = 0; i < 10000; ++i)
			s += char(dist(gen));
		cout << "Case #" << q << ": " << calc(s) << "\n";
	}
	cout << "Done for " << (clock() - beg) * 1.0 / CLOCKS_PER_SEC;
}

int main() {
	ios_base::sync_with_stdio(false);
	//test();
	solve();
	return 0;
}