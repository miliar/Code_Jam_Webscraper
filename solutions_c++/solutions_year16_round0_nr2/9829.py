#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
		int count = 0;
		char p, q;
		for (int j = 0; j < s.length(); j++) {
			if (j == s.length() - 1) {
				if (s[j] == '-') {
					count += 1;
				}
				break;
			}
			if (s[j] == '-' && s[j + 1] == '+') {
				count += 1;
			}
			else if (s[j] == '+' && s[j + 1] == '-') {
				count += 1;
			}
		}
		
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}