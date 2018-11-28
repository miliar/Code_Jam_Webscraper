#include <iostream>
#include <set>

using namespace std;

int main() {
	int T, cnt = 0;
	cin >> T;
	while (T--) {
		string s;
		cin >> s;
		cout << "Case #" << ++cnt << ": ";
		s += '+';
		int ans = 0;
		for (int i = 0; i + 1 < s.size(); i++)
			if (s[i] != s[i + 1])
				ans++;
		cout << ans << endl;
	}
}
