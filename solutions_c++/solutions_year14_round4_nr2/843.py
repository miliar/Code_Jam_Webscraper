#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int n, a[10000], r = 0, i;

		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> a[i];
		}

		int il = 0, ir = n, j, jm;

		for (i = 0; i < n; i++) {
			jm = il;
			for (j = il; j < ir; j++) if (a[j] < a[jm]) jm = j;
			if (jm - il < ir - jm - 1) {
				r += jm - il;
				for (j = jm; j > il; j--) swap(a[j - 1], a[j]);
				il++;
			} else {
				r += ir - jm - 1;
				for (j = jm; j < ir - 1; j++) swap(a[j], a[j + 1]);
				ir--;
			}
		}

		// for (i = 0; i < n; i++) cout << a[i] << ' '; cout << endl;
		cout << "Case #" << it << ": " << r << endl;
	}
}
