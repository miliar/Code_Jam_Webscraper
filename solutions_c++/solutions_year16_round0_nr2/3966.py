#include<iostream>
#include<string>
#include<vector>
#include<algorithm>


void solve(int c) {
	std::string s;
	std::cin >> s;

	long long count = 0;
	while (std::find(s.begin(), s.end(), '-') != s.end()) {
		// + ‚ª‰½ŒÂ‚ ‚é‚©
		if (s[0] == '+') {
			count++;
			for (int i = 0; i < s.length(); i++) {
				if (s[i] == '-') break;
				s[i] = '-';
			}
		}
		int b = s.length() - 1;
		for (; b > 0; b--) {
			if (s[b] != '+') break;
		}

		for (int i = 0; i <= b; i++) {
			if (i == b) {
				if (s[i] == '+') s[i] = '-';
				else s[i] = '+';
			} else if (s[i] == '-') {
				if (s[b] == '+') {
					s[i] = '-';
				} else {
					s[i] = '+';
				}
				s[b] = '+';
			} else {
				if (s[b] == '+') {
					s[i] = '-';
				} else {
					s[i] = '+';
				}
				s[b] = '-';
			}
			b--;
		}
		count++;
	}
	std::cout << "Case #" << c << ": " << count << std::endl;
}

int main() {
	int t;

	std::cin >> t;

	for (int i = 0; i < t; i++) {
		solve(i + 1);
	}
}