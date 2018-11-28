#include <iostream>
#include <vector>
#include <string>

using namespace std;
int N;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int ans = 0;
		int cur = 0;
		cin >> N;
		string s;
		cin >> s;
		cur += s[0] - '0';
		for (int i = 1; i <= N; ++i) {
			if (cur < i) {
				ans += i - cur;
				cur = i + (s[i] - '0');
			} else {
				cur += (s[i]) - '0';
			}

		}

		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}
