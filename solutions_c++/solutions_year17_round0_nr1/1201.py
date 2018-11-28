#include <iostream>
#include <string>
#include <vector>

using namespace std;

int calc(const string &s, int k) {
	int res = 0, sum = 0;
	int size = s.size();
	vector<int> flip(size, 0);
	for (int idx = 0; idx+k <= size; ++idx) {
		int n = (s[idx] == '-') ? 1 : 0;
		if ((n + sum)%2 != 0) {
			++res;
			flip[idx] = 1;
		}

		sum += flip[idx];
		if (idx-k+1 >= 0) {
			sum -= flip[idx-k+1];
		}
	}

	for (int idx = size-k+1 ; idx < size; ++idx) {
		int n = (s[idx] == '-') ? 1 : 0;
		if ((n + sum)%2 != 0) {
			return -1;
		}

		if (idx-k+1 >= 0) {
			sum -= flip[idx-k+1];
		}
	}

	return res;
}

int main() {
	int t, k;
	string s;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	for (int i = 1; i <= t; ++i) {
		cin >> s >> k;  // read n and then m.
		int ret = calc(s, k);
		cout << "Case #" << i << ": ";
		if (ret == -1) {
			cout <<  "IMPOSSIBLE";
		} else {
			cout << ret;
		}
		cout << endl;
	}

	return 0;
}

