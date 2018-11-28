#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		string s;
		cin >> n >> s;
		int invited = 0, total = 0;
		for (int i = 0; i < n + 1; i++) {
			int c = s[i] - '0';
			int newInvited = (c > 0 && i > total) ? (i - total) : 0;
			invited += newInvited;
			total += newInvited + c;
		}
		printf("Case #%d: %d\n", t, invited);
	}
	return 0;
}
