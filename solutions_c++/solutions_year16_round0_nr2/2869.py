#include <iostream>
#include <string>

using namespace std;

void solve()
{
	string s;
	cin >> s;
	int ans = 0;
	for (int i = s.size() - 1; i >= 0; i--) {
		if (s[i] == '-') {
			if (s[0] == '+') {
				ans++;
				for (int j = 0; j < i && s[j] == '+'; j++) s[j] = '-';
			}
			for (int j = 0; j <= i; j++) {
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
			char c;
			for (int j = 0; j <= i / 2; j++) {
				c = s[j];
				s[j] = s[i - j];
				s[i - j] = c;
			}
			ans++;
		}
	}
	cout << ans << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
