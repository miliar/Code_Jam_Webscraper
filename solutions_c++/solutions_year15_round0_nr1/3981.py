#include <iostream>
#include <string>
using namespace std;

int solve() {
	int n;
	string s;
	cin >> n >> s;

	int d = 0;
	int ans = 0;

	for (int i = 0; i <= n; ++i) {
		if (s[i] > '0') {
			if (i > d) {
				ans += i - d;
				d = i;
			}
			
			d += s[i] - '0';
		}
	}

	return ans;
}

int main() {
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": " << solve() << endl;
	}
}