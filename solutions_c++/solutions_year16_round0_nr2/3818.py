#include <bits/stdc++.h>

using namespace std;

void flip(string::iterator l, string::iterator r) {
	reverse(l, r);

	while(l != r) {
		if(*l == '+') {
			*l = '-';
		}
		else {
			*l = '+';
		}
		l++;
	}
}

void solve(string s) {
	int flips = 0;

	auto r = s.end();

	while(r != s.begin()) {
		if(*(r-1) == '+') {
			r--;
		}
		else {
			if(s[0] == '-') {
				flip(s.begin(), r);
				flips++;
			}
			else {
				auto e = s.begin();
				while(*e == '+') {
					e++;
				}

				flip(s.begin(), e);
				flips++;
			}
		}
	}

	cout << flips << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		string s;
		cin >> s;
		solve(s);
	}

	return 0;
}
