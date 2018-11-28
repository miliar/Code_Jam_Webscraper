#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int j = 0; j < t; j++) {
		int k, c, s;
		cin >> k >> c >> s;

		cout << "Case #" << j + 1 << ": ";
		for (int i = 0; i < s; i++) {
			cout << i + 1 << (i == s - 1 ? '\n' : ' ');
		}
	}

	return 0;
}
