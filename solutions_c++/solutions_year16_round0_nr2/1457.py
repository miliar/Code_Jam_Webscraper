#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		int c = 0;
		for (int k = 0; k < s.length(); k++) {
			if (s[k] == '-' && (k == s.length() - 1 || s[k+1] == '+'))
				c++;
		}
		int res = 2 * c;
		if (s[0] == '-') res--;
		printf("Case #%d: %d\n", i, res);
	}
}
