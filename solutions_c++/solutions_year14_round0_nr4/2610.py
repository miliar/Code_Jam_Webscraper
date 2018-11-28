#include <fstream>
//#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

ifstream cin("D-large.in");
ofstream cout("output.txt");


void solve(int t) {
	int n;
	cin >> n;
	double a[1100], b[1100];
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	for (int i = 0; i < n; ++i) {
		cin >> b[i];
	}
	int low = 0;
	int aa = 0;
	int bb = 0;
	sort(a, a+n);
	sort(b, b+n);
	while(bb < n) {
		while(b[bb] < a[aa] && bb < n)
			++bb;
		if (bb < n) {
			++bb;
			++aa;
		}
	}
	int l = 0;
	int r = n + 1;
	while (r - l > 1) {
		int m = (l + r) / 2;
		int shift = n - m;
		for (int i = 0; i < m; ++i) {
			// should be a[shift + i] > b[i]
			if (a[shift + i] < b[i]) {
				r = m;
				break;
			}
		}
		if (r != m) {
			l = m;
		}
	}

	//cout << n - aa << endl;

	cout << "Case #" << t << ": " << l << ' ' << n - aa << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		solve(i+1);
	}
	return 0;
}