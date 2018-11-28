#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int ii=1; ii <= t; ii++) {
		printf("Case #%d: ", ii);
		string s;
		cin >> s;
		int ans = 0;
		for (int i=s.length()-1; i>=1; i--) {
			if (s[i] == '-' && s[i-1] == '+') ans += 2;
		}
		ans += s[0] == '-';
		cout << ans << endl;
	}
}
