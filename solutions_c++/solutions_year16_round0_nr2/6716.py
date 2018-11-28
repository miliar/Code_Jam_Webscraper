#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
		string s2 = "";
		for (int j = 0; j < s.size(); j++) {
			s2 += s[j];
			for (int k = j+1; k < s.size(); k++) {
				if (s[j] == s[k]) {
					j++;
				} else {
					break;
				}
			}
		}
		int kk = 0;
		int sz = s2.size();
		if (s2[0] == '+') {
			if (sz % 2 == 0) {
				kk = sz;
			} else {
				kk = sz-1;
			}
		} else {
			if (sz % 2 == 0) {
				kk = sz-1;
			} else {
				kk = sz;
			}
		}
		printf("Case #%d: %d\n", i+1, kk);
	}
	return 0;
}