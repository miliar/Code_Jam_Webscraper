#include <iostream>
#include <string>

using namespace std;

void solve(const int t, string& str) {
	string res;
	res += str[0];
	for (size_t i = 1, sz = str.size(); i < sz; ++i) {
		if (str[i] >= res[0]) {
			res = str[i] + res;
		} else {
			res += str[i];
		}
	}
	cout << "Case #" << t << ": " << res << endl;
}

int main() {
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		string str;
		cin >> str;
		solve(i + 1, str);
	}

	return 0;
}
