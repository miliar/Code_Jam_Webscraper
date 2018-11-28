#include <iostream>

using namespace std;

void solve()
{
	int n;
	int p[26] = {0};
	int psum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> p[i];
		psum += p[i];
	}
	while (psum > 0) {
		int max1 = -1, max2 = -1;
		for (int i = n - 1; i >= 0; i--) {
			if ((max1 == -1 && p[i] > 0) || p[i] >= p[max1]) {
				max2 = max1;
				max1 = i;
			}
		}
		if (max1 > -1) {
			cout << (char)(max1 + 'A');
			if (p[max1] == p[max2] && psum > 3 || psum == 2) {
				cout << (char)(max2 + 'A');
				p[max2]--;
				psum--;
			}
			p[max1]--;
			psum--;
		}
		if (psum == 1) {
			for (int i = 0; i < n; i++) {
				if (p[i] > 0) {
					cout << (char)(i + 'A');
					p[i]--;
					psum--;
					break;
				}
			}
		}
		cout << " ";
	}
	cout << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
