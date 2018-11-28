#include <iostream>
#include <string>
#include "stdio.h"

using namespace std;

string solve(string s) {
	if (s.length() <= 1)
		return s;

	char maxchar='A'-1;
	int pt = -1;

	for (int i = s.length() - 1; i >= 0; --i)
		if (s[i] > maxchar) {
			maxchar = s[i];
			pt = i;
		}

		return s.substr(pt, 1) + solve(s.substr(0, pt)) + s.substr(pt + 1);
}

int main() {
	int t;
	cin >> t;

	string s;
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> s;

		cout << "Case #" << tcount << ": " << solve(s) << endl;
	}

	return 0;
}