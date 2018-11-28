#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		int n_times = 1;
		for (int i = 1; i < (int)s.length(); i++) {
			if (s[i] != s[i - 1]) {
				n_times++;
			}
		}
		if (s[s.length() - 1] == '+') {
			n_times--;
		}
		cout << "Case #" << i << ": " << n_times << '\n';
	}
	return 0;
}
