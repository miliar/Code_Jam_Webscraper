#include <iostream>
#include <string>
using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		int n, ans = 0, cnt = 0;
		string shy;
		cin >> n >> shy;
		for (int i = 0; i <= n; i++) {
			int tmp = shy[i] - '0';
			if ((cnt += tmp) < (i + 1)) {
				ans += i + 1 - cnt;
				cnt = i + 1;
			}
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}
}