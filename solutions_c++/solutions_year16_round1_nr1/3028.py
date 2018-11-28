#include <iostream>
#include <string>
using namespace std;

int main() {
	int t; cin >> t;
	for (int tloop = 1; tloop <= t; ++tloop) {
		string s, ret = ""; cin >> s;
		ret = s[0];
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] >= ret[0]) ret = s[i] + ret;
			else ret = ret + s[i];
		}
		cout << "Case #" << tloop << ": " << ret << endl;
	}
}