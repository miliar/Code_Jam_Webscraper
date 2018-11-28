#include <iostream>
#include "stdio.h"

using namespace std;

int main() {
	int t;
	cin >> t;

	int s;
	for (int tcount = 1; tcount <= t; ++tcount) {
		int mk[1024] = {0};
		cin >> s;

		int count = 0, ans = 0;
		getchar();
		for (int i = 0; i <= s; ++i) {
			int tp = getchar() - '0';
			if (tp == 0)
				continue;
			if (count >= i) {
				count += tp;
			}
			else {
				ans += i - count;
				count = i+tp;
			}
		}

		cout << "Case #" << tcount << ": " << ans << endl;
	}

	return 0;
}