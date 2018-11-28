#include <bits/stdc++.h>

using namespace std;

int main() {
	int countTests;
	cin >> countTests;

	for (int test = 1; test <= countTests; test++) {
		string s;
		cin >> s;

		s += '+';

		int answer = 0;

		for (size_t i = 1; i < s.size(); i++) {
			answer += (s[i] != s[i - 1]);
		}


		cout << "Case #" << test << ": " << answer << "\n";
	}
	return 0;
}