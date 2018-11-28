#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t,tc;
	string s;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> s;
		int l = s.length();
		int c = 1;
		for (int i = 0; i < l-1; i++) {
			if (s[i] != s[i+1]) {
				c++;
			}
		}
		if (s[l-1] == '+') {
			printf("Case #%d: %d\n", tc, c-1);
		} else {
			printf("Case #%d: %d\n", tc, c);
		}
	}
}