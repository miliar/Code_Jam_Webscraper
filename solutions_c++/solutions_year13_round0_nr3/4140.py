#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

int T;
long long A, B;

inline bool isPalin(string s) {
	for (int i = 0; i < s.length() / 2; i++) {
		if (s[i] != s[s.length() - 1 - i]) {
			return false;
		}
	}
	return true;
}

long long ans;

inline bool check(string str) {
	long long x = _atoi64(str.c_str());
	long long square = x * x;
	if (square > B) {
		return false;
	}
	stringstream stream2;
	stream2 << square;
	if (isPalin(stream2.str()) && square >= A && square <= B) {
		ans++;
	}
	return true;
}

int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> A >> B;
		ans = 0;
		if (A <= 1 && B >= 1) ans++;
		if (A <= 4 && B >= 4) ans++;
		if (A <= 9 && B >= 9) ans++;
		for (int i = 1; ; i++) {
			stringstream stream;
			stream << i;
			string str = stream.str();
			string rev = string(str.rbegin(), str.rend());
			string str2 = str + rev;
			if (!check(str2)) {
				break;
			}
			for (char j = '0'; j <= '9'; j++) {
				str2 = str + j + rev;
				check(str2);
			}
		}
		cout << ans << endl;
	}
}