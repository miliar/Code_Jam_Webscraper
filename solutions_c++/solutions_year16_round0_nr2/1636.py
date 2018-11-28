
#include <iostream>
#include <string>

using namespace std;

inline char antip(char c) {
	return '+' + '-' - c;
}

void flip(string &s, int len) {
	for (int i = 0; i < (len+1)/2; i++) {
		char c = antip(s[len-i]);
		s[len-i] = antip(s[i]);
		s[i] = c;
	}
	if (len % 2 == 0) {
		s[len/2] = antip(s[len/2]);
	}
}

int magic(string &s, int done) {
	int max = s.length() - done;
	if (max == 0) return 0;

	int b = max - 1;
	while (s[b] == '+' && b > 0) b--;
	if (b == 0) return (s[0] == '+' ? 0 : 1);

	if (s[0] == '-') {
		flip(s, b);
		return 1 + magic(s, done + 1);
	}

	// guaranteed to start with '+' and end with '-'
	int a = 0;
	while (s[a] == '+') s[a++] = '-'; // flip all +s at the beginning
	flip(s, b);
	return 2 + magic(s, done + a);
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		cout << magic(s, 0) << endl;
	}

	return 0;
}
