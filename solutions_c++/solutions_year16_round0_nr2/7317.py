#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,r;
	cin >> t;
	for (r = 1; r <= t; r++) {
		string s;
		cin >> s;
		s = s + '+';
		long long int i,c=0;
		for (i = 0; i < s.length()-1; i++) {
			if (s[i] != s[i+1]) {
				c++;
			}
		}
		cout << "Case #" << r << ": " << c << endl;
	}
	return 0;
}
