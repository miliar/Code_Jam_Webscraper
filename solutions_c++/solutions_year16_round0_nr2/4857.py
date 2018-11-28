#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		string s;
		while (s.empty()) {
			getline(cin, s);
		}
		while (s.size() > 0 && s.back() == '+') {
			s.erase(s.begin() + s.size() - 1);
		}

		int count = 0;
		if (s.size() > 0) {
			++count;
		}
		for (size_t i = 0; i + 1< s.size(); ++i) {
			if (s[i] != s[i + 1]) {
				++count;
			}
		}
		cout << "Case #" << test << ": " << count << endl;
	}
}
