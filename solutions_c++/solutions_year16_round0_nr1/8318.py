#include <bits/stdc++.h>
using namespace std;


int main () {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n;
		vector<bool> v(10, false);
		int count = 0;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		int m, j;
		for (m = n, j = 1; count < 10; ++j, m = j*n) {
			while (m) {
				int digit = m%10;
				m = m/10;
				if (!v[digit]) {
					count++;
					v[digit] = true;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << n*(j-1) << endl;
	}
	return 0;
}




