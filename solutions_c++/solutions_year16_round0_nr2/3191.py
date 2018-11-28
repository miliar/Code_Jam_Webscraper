#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int k = 0; k < t; k++) {
		string s;
		cin >> s;

		int n = s.size();

		int i = 0;
		int r = 0;

		while (i < n) {
			if (s[i] == '-') {
				r = i;
			}
			i++;
		}

		int flip = 0;

		while (r >= 0) {
			if (s[r] =='-') {
				for (int j = 0; j <= r; j++) {
					if (s[j] == '-') {
						s[j] = '+';
					} else if (s[j] == '+') {
						s[j] = '-';
					}
				}
				flip++;
			}
			r--;
		}
		cout << "Case #" << k + 1 << ": " << flip << endl;
	}

	return 0;
}
