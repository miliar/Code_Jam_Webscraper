#include <iostream>
#include <string>

using namespace std;

void solve()
{
	string s;
	cin >> s;
	string ans;
	ans += s[0];
	for (int i = 1; i < s.size(); i++) {
		if (s[i] >= ans[0]) {
			ans = s[i] + ans;
		} else {
			ans = ans + s[i];
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
