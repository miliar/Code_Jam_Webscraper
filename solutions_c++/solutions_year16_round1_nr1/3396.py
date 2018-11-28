#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-out-l.txt", "w", stdout);

	int t;
	cin >> t;

	for (int j = 0; j < t; j++) {
		string s;
		cin >> s;

		int n = s.size();
		string a = "";

		a += s[0];

		for (int i = 1; i < n; i++) {
			if (s[i] >= a[0]) {
				a = s[i] + a;
			} else {
				a = a + s[i];
			}
		}

		cout << "Case #" << j + 1 << ": " << a << endl;
	}

	return 0;
}

