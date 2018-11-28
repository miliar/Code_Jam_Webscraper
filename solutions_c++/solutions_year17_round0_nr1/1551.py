#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector

void flip(char& get)
{
	if (get == '+') get = '-';
	else get = '+';
}

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		rep(i, s.length() + 1 - k) {
			if (s[i] == '+') continue;
			ans++;
			rep(j, k) flip(s[i + j]);
		}
		int flag = 1;
		rep(i, k) if (s[s.length() - 1 - i] == '-') flag = 0;
		if (flag) cout << "Case #" << t + 1 << ": " << ans << endl;
		else cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
