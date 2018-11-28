#include <iostream>
#include <string>
#include <cassert>
using namespace std;

void flip(string &s, int i, int K) {
	assert(i + K <= (int)s.size());
	for (int j = 0; j < K; ++j) {
		s[i + j] = (s[i + j] == '+' ? '-' : '+');
	}
}

int main() {
	int testsCount;
	cin >> testsCount;
	for (int test = 0; test < testsCount; ++test) {
		string s;
		int K;
		cin >> s >> K;
		int res = 0;
		for (int i = 0; i + K <= (int)s.size(); ++i) {
			if (s[i] == '-') {
				flip(s, i, K);
				res += 1;
			}
		}
		cout << "Case #" << test + 1 << ": ";
		if (s.find("-") == string::npos)
			cout << res;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}