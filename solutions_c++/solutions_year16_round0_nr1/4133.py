#include <algorithm>
#include <cmath>
#include <memory.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;

int cnt[15];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int tst = 1; tst <= test; ++tst) {
		cout << "Case #" << tst << ": ";
		int n;
		cin >> n;
		if (n == 0) {
			cout << "INSOMNIA" << endl;	
		} else {
			ll res = -1;
			memset(cnt, 0, sizeof(cnt));
			for (int i = 1; true; ++i) {
				ll val = (ll)i * (ll)n;
				while (val) {
					cnt[val % 10] = 1;
					val /= 10;
				}
				bool ok = true;
				for (int q = 0; q <= 9; ++q)	if (cnt[q] == 0) ok = false;
				if (ok) res = (ll)i * (ll)n;
				if (ok) break;
			}
			cout << res << endl;
		}
	}
	return 0;           
}