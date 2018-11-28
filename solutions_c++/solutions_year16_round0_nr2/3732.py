//============================================================================
// Name        : q1b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	int i;
	string s;
	char c;

	cin >> T;

	for (int t = 0; t < T; t++) {
		cin >> s;
		int cost = 0;
		int len = s.length();
		for (i = 1; i < len; i++) {
			if (s[i] != s[i-1]) {
				cost++;
			}
		}
		if (s[len-1] == '-') {
			cost++;
		}
		cout << " Case #" << t+1 << ": " << cost << endl;
	}
	return 0;
}
