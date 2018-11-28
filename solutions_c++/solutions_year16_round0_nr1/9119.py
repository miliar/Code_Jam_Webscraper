#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int t, it = 1;
	cin >> t;
	while (t) {
		vector<int> was(10, 0);
		int n, m, cnt = 0;
		cin >> n;
		m = n;
		cout << "Case #" << it << ": ";
		if (n == 0) {
			cout << "INSOMNIA\n";
		} else {
			while (cnt < 10) {
				cnt = 0;
				int num = n;
				while (num) {
					was[num % 10] = 1;
					num /= 10;
				}
				//cout << n << "\n";
				for (int i = 0; i < 10; i++) {
					//cout << was[i] << ' ';
					cnt += was[i];
				}
				//cout << '\n';
				n += m;
			}
			cout << n - m << '\n';
		}
		it++;
		t--;
	} 
	return 0;
}