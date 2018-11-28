#include <bits/stdc++.h>

using namespace std;


int main() {
	int T;
	cin >> T;

	string s;
	for (int i = 0; i < T; i++) {
		cin >> s;

		deque<char> ret;
		char score = 0;
		for (int j = 0; j < s.size(); j++) {
			if (s[j] >= score) {
				ret.push_front(s[j]);
				score = s[j];
			} else {
				ret.push_back(s[j]);
			}
		}

		cout << "Case #" << (i+1) << ": ";

		for (auto&& c : ret) {
			cout << c;
		}
		cout << endl;
	}

	return 0;
}