#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;

		s.push_back('+');
		int changes = 0;
		for (int i = 1; i < s.length(); i++)
			changes += (s[i] == s[i-1] ? 0 : 1);

		cout << "Case #" << t << ": " << changes << '\n';
	}

	return 0;
}
