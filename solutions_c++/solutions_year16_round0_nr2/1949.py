#include <iostream>

using namespace std;

char toggle(char c) {
	return ((c == '+') ? '-' : '+');
}

int solve(string s) {
	int count = 0; int i;
	bool flip = false;
	for (i = s.size()-1; i >= 0; i--) {
		if (s[i] == '-' && !flip) {
			flip = true;
		}
		if (flip) {
			s[i] = toggle(s[i]);
		}
	}
	
	if (!flip) {
		return 0;
	} else {
		reverse(s.begin(), s.begin()+i);
		return 1 + solve(s);
	}
}

int main() {
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++) {
		string p; cin >> p;
		cout << "Case #" << t << ": " << solve(p) << "\n";
	}
}