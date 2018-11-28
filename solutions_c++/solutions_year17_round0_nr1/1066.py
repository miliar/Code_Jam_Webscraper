#include <iostream>
#include <string>

using namespace std;

string s;
int k;

void solve() {
	cin >> s >> k;
	int p = 0;
	while (p < s.size() && s[p] == '+')
		p++;
	s = s.substr(p);
	int len = s.size();
	while (len > 0 && s[len - 1] == '+')
		len--;
	int res = 0;
	while (len >= k) {
		for (int i = 0; i < k; i++)
			s[len - i - 1] = (s[len - i - 1] == '+' ? '-' : '+');
		res++;
		while (len > 0 && s[len - 1] == '+')
			len--;
	}
	if (len)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
