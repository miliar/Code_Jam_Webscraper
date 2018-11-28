#include <bits/stdc++.h>

using namespace std;

void solve(int n) {
	if(n == 0) {
		cout << "INSOMNIA" << endl;
	}
	else {
		set<int> digits;

		int i = 1;
		while(digits.size() < 10) {
			int k = n * i;
			while(k != 0) {
				digits.insert(k % 10);
				k /= 10;
			}

			i++;
		}

		cout << n * (i - 1) << endl;
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		int n;
		cin >> n;
		solve(n);
	}

	return 0;
}
