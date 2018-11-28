#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s[8];
int a[8];
int x[10000];

bool next(int p, int n) {
	if (p < 0) return false;
	a[p]++;
	if (a[p] >= n) {
		a[p] = 0;
		return next(p-1, n);
	}
	return true;
}

void solve() {
	fill_n(x, 10000, 0);
	int m, n;
	cin >> m >> n;
	for (int i=0; i<m; i++) {
		cin >> s[i];
		a[i] = 0;
	}
	sort(s, s+m);
	do {
		int xval = 0;
		for (int i=0; i<m; i++) {
			for (size_t j=0; j<=s[i].length(); j++) {
				bool dupl = false;
				for (int k=0; k<i; k++) {
					if (a[i] == a[k] && s[i].substr(0, j) == s[k].substr(0, j)) {
						dupl = true;
						break;
					}
				}
				if (!dupl) xval++;
			}
		}
		x[xval]++;
	} while (next(m-1, n));
	for (int i=10000; i>=0; --i) {
		if (x[i] > 0) {
			cout << i << " " << x[i];
			return;
		}
	}
	cout << "0 1";
}

int main() {
	int t;
	cin >> t;
	for (int cn=1; cn<=t; cn++) {
		cout << "Case #" << cn << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}