#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int tc, t = 0;
    cin >> tc;
    while (tc--) {
		string s;
		cin >> s;
		int count = 0, len = s.length() - 1;
		for (int i = len; i >= 0; i--) {
			if (s[i] == '-') {
				for (int j = i; j >= 0; j--) {
					s[j] = (s[j] == '+') ? '-' : '+';
				}
				count++;
			}
		}
		cout << "Case #" << (++t) << ": " << count << endl;
	}
	return 0;
}
