#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int T;
string s;

int main() {
	cin >> T;
	for (int it = 1; it <= T; it++) {
		cin >> s;
		int counter = 0;
		char lastSign = '+';
		for (int j = s.size() - 1; j >= 0; j--) {
			if (s[j] != lastSign) {
				counter++;
				if (lastSign == '+') {
					lastSign = '-';
				}
				else {
					lastSign = '+';
				}
			}
		}
		printf("Case #%d: %d\n", it, counter);
	}	
	return 0;
}