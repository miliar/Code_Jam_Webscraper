#include <iostream>
using namespace std;
int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		string s;
		cin >> s;
		int cnt = 0;
		char c = '+';
		for (int i = (int)s.size() - 1; i >= 0; i--) {
			if (s[i] == c) continue;
			else {
				cnt++;
				if (c == '+') c = '-';
				else c = '+';
			}
		}
		printf("Case #%d: ", tc);
		printf("%d\n", cnt);
	}
	return 0;
}
