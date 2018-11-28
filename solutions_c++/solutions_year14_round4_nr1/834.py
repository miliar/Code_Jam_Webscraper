#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int x, n, s[10000], i, ja, jb;

		cin >> n >> x;
		for (i = 0; i < n; i++) {
			cin >> s[i];
		}
		sort(s, s + n);

		for (i = ja = 0, jb = n - 1; ja <= jb; i++) {
			if (ja < jb && s[ja] + s[jb] <= x) {
				ja++, jb--;
			} else {
				jb--;
			}
		}

		cout << "Case #" << it << ": " << i << endl;
	}
}