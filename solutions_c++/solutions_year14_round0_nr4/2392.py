#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int n;
double a[1005];
double b[1005];

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cout << "Case #" << test << ": ";
		cin >> n;
		for (int i = 0; i < n; ++i) cin >> a[i];
		for (int i = 0; i < n; ++i) cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		int res = 0;
		int p = 0;
		for (int i = 0; i < n; ++i) {
			if (a[i] > b[p]) {
				++res;
				++p;
			}
		}
		cout << res << " ";
		res = 0;
		p = n - 1;
		for (int i = n - 1; i >= 0; --i) {
			if (a[i] > b[p]) {
				++res;
			} else {
				--p;
			}
		}
		cout << res << endl;
	}
	return 0;
}