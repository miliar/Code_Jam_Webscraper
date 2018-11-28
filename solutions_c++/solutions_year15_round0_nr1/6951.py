#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int solve(const int num, const string& s) {
	int need = 0, cnt = 0;
	for (int i = 0; i <= num; ++i) {
		 int t = max(i - cnt, 0);
		 need += t;
		 cnt += s[i] - '0' + t;
	}
	return need;
}

void main() {
	int T = 0;
	cin >> T;

	int num = 0;
	string s = "";
	for (int i = 0; i < T; ++i) {
		cin >> num >> s;
		cout << "Case #" << i + 1 << ": " << solve(num, s) << endl;
	}
}