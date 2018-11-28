#include <string>
#include <iostream>
using namespace std;

bool done(string &s) {
	for (size_t i = 0; i < s.size(); i++)
		if (s[i] == '-') return 0;
	return 1;
}

int main() {
	freopen("B-large.in", "r", stdin);
	int T; cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		string s; cin >> s;
		cout << "Case #" << tt << ": ";
		int ret = 0;
		while (!done(s)) {
			string postfix = "";
			string prefix  = "";
			for (int i = s.size()-1; i >= 0; i--)
				if (s[i] == '-') {
					prefix = s.substr(0, i+1);
					break;
				} else postfix += '+';
			s = "";
			if (prefix[0] == '+') {
				ret ++;
				for (size_t i = 0; i < prefix.size(); i++)
					if (prefix[i] == '-') break;
					else prefix[i] = '-';
			}
			for (size_t i = 0; i < prefix.size(); i++) {
				char c = prefix[i]=='-'?'+':'-';
				s = c+s;
			}
			s += postfix;
			ret ++;
		}
		cout << ret << endl;
	}
	return 0;
}
