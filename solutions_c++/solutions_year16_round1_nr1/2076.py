#include <vector>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	string s;
	string last;
	
	cin >> tests;
	for (int t = 1; t <= tests; t++) {
		cin >> s;
		
		last = s[0];

		for (int i = 1; i < s.length(); i++) {
			if (s[i] >= last[0]) {
				last = s[i] + last;
			}
			else {
				last = last + s[i];
			}
		}

		cout << "Case #" << t << ": " << last << "\n";
	}

	return 0;
}