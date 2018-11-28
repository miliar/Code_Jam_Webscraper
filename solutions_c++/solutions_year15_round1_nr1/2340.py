#include <bits/stdc++.h>

using namespace std;

int main() {
#ifndef ONLINE_JUDEGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	long long t;
	cin >> t;
	for (long long i = 1; i <= t; i++) {
		long long x = 0, diff = 0, y = 0;
		long long n;
		cin >> n;
		long long ar[n];
		for (long long z = 0; z < n; z++)
			cin >> ar[z];
		ar[n] = ar[n - 1];
		for (long long z = 0; z < n; z++) {
			if (ar[z] > ar[z + 1])
				x += ar[z] - ar[z + 1];
			diff = max(diff, ar[z] - ar[z + 1]);
		}
		for (long long z = 0; z < n - 1; z++) {
			y += min(ar[z], diff);
		}
		cout << "Case #" << i << ": " << x << " " << y << endl;
	}
	return 0;
}
