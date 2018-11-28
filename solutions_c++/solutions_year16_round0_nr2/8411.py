#include <bits/stdc++.h>
using namespace std;


int main () {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		cin >> s;
		s += '+';
		int count = 0;
		for (int i = s.size() -1; i > 0; --i) {
			if (s[i] != s[i - 1]) count++;
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
}




