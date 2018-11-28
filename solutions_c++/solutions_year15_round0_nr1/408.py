#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void solve() {
	int sm; cin >> sm;
	string s; cin >> s;

	int res = 0;
	int sum = 0;
	for (int i = 0; i <= sm; ++i) {
		int t = s[i] - '0';
		if (t > 0 && sum < i) {
			res += i - sum;
			sum = i;
		}
		sum += t;
	}

	static int test;
	cout << "Case #" << ++test << ": " << res << endl;
}

int main() {
	int t;
	cin >> t;
	while (t --> 0)
		solve();
	return 0;
}