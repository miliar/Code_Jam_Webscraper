#include <iostream>

using namespace std;
int t;
int main() {
	cin >> t;
	int s1 = 0, s2 = 0, n, r = 0;
	int m[101];
	for (int i = 1; i <= t; i++) {
		cin >> n;
		for (int j = 0; j < n; j++) {
			cin >> m[j];
		}
		s1 = 0;
		s2 = 0;
		r = 0;
		for (int j = 0; j < n - 1; j++) {
			if (m[j + 1] < m[j])
				s1 += m[j] - m[j + 1];
			if (r < (m[j] - m[j + 1])) {
				r = m[j] - m[j + 1];
			}
		}

		for (int j = 0; j < n - 1; j++) {
			if (m[j] < r)
				s2 += m[j];
			else if (m[j] >= r)
				s2 += r;
		}

		cout << "Case #" << i << ": " << s1 << " " << s2 << endl;
	}
}
