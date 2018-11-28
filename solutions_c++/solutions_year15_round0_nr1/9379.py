#include <bits/stdc++.h>

using namespace std;

/*
 There's No Impossible
 Once You Start Trying
 */

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "w", stdout);
	int cases, max, sum = 0, g = 0, num, w = 1;
	string s;
	cin >> cases;
	while (cases--) {
		cin >> max >> s;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '0') {
				num = 0;
			} else if (s[i] == '1') {
				num = 1;
			} else if (s[i] == '2') {
				num = 2;
			} else if (s[i] == '3') {
				num = 3;
			} else if (s[i] == '4') {
				num = 4;
			} else if (s[i] == '5') {
				num = 5;
			} else if (s[i] == '6') {
				num = 6;
			} else if (s[i] == '7') {
				num = 7;
			} else if (s[i] == '8') {
				num = 8;
			} else if (s[i] == '9') {
				num = 9;
			}
			if (sum >= i) {
				sum += num;
			} else {
				g += (i - sum);
				sum += (i - sum);
				sum += num;
			}
		}
		cout << "Case #" << w << ": " << g << endl;
		w++;
		sum = 0;
		g = 0;
	}
	return 0;
}
