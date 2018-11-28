#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	string s;

	for (int i = 0; i < T; i++) {
		cin >> s;
		char group = '/';
		int count = 0;
		for (int j = 0; j < s.size(); j++) {
			if (s[j] != group) {
				count++;
				group = s[j];
			}
		}
		cout << "Case #" << (i + 1) << ": " << count - (group == '+' ? 1 : 0) << endl;
	}

	return 0;
}