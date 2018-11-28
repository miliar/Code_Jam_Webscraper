#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

vector<long long> p;

bool isp(long long x) {
	stringstream ss;
	string s;
	ss << x;
	ss >> s;
	for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
		if (s[i] != s[j]) {
			return false;
		}
	}
	return true;
}

void init() {
	p.push_back(-1);
	for (int i = 1; i <= 10000001; ++i) {
		if (isp(i) && isp(1LL * i * i)) {
			p.push_back(1LL * i * i);
			cerr << i << ' ' << (1LL * i * i) << endl;
		}
	}
}

int gao(long long a) {
	return upper_bound(p.begin(), p.end(), a) - p.begin() - 1;
}

int main() {
	init();
	int Tc;
	cin >> Tc;
	for (int re = 1; re <= Tc; ++re) {
		long long a, b;
		cin >> a >> b;
		cout << "Case #" << re << ": "
			<< gao(b) - gao(a - 1)
			<< endl;
	}
}
