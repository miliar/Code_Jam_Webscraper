#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int T, n, m;
string shy;
int main() {
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> m;
		cin >> shy;
		int cnt = shy[0] - 48;
		int ans = 0;
		for (int i = 1; i <= m; i++) {
			int k = shy[i] - 48;
			if (k > 0 && cnt < i) {
				int need = i - cnt;
				ans += need;
				cnt += k + need;
			}
			else {
				if (k > 0) cnt += k;
			}
		}

		cout << "Case #" << test << ": " << ans << endl; 
	}
	return 0;
}
