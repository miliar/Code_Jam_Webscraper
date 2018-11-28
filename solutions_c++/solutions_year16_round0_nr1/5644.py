#include <bits/stdc++.h>
using namespace std;

#define vi vector<int>

int main() {
	// int T = 100;
	// cout << T << endl;
	// while (T--) {
	// 	cout << rand()%1000000+1 << endl;
	// }
	// return 0;
	int t, n;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		cin >> n;
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int bs = (1 << 10) - 1;
		long long m;
		for (int k = 1; k <= 1000; k++) {
			m = n * k;
			for (int j = 0; j < floor(log10(m))+1; j++) {
				int d = m % int(pow(10, j+1)) / pow(10, j);
				bs &= ~(1 << d);
			}
			if (bs == 0) {
				cout << m << endl;
				break;
			}
		}
	}
	return 0;
}
