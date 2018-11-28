#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	int test;
	cin >> test;
	for (int test_case = 1; test_case <= test; ++test_case) {
		int n;
		cin >> n;
		cout << "Case #" << test_case << ": ";
		if (n == 0) cout << "INSOMNIA" << endl;
		else {
			char bl[11] = {};
			for (int i = 1; ; ++i) {
				ll t = i * 1LL * n;
				while (t != 0) {
					bl[t % 10] = 1;
					t /= 10;
				}
				char check = 1;
				for (int j = 0; j < 10; ++j)
					check &= bl[j];
				if (check) {
					cout << (i * 1LL * n) << endl;
					break;
				}
			}
		}
	}
	return 0;
}
