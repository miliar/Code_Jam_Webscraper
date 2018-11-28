#include <iostream>

using namespace std;

string mergeString(string s) {
	int n = s.size(), i = 0;
	string res = "";
	while( i < n) {
		char c = s[i];
		while (c == s[i] && i < n) {
			++i;
		}
		res += c;
	}
	return res;
}

string flip (string s) {
	string res = "";
	for(int i = s.size() - 1; i >= 0; --i) {
		res += s[i] == '+' ? '-' : '+';
	}
	return res;
}

int main (int argc, char * argv[]) {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		string s;
		cin >> s;
		s = mergeString(s);
		int ans = 0;
		while(s.size() >= 2) {
			char b = s[0], e = s[s.size() - 1];
			s = s.substr(1, s.size() - 2);
			if (e == '+') {
				s = mergeString(b + s);
			} else {
				if (b == '+') {
					ans += 2;
				} else {
					ans += 1;
				}
				s = mergeString('+' + flip(s));
			}
			// cout << s << endl;
		}
		if (s.size() == 1) {
			ans += s[0] == '-';
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}