//In the name of God
//...
#include <algorithm>
#include <iostream>
using namespace std;
const int N = 1e3 + 3;


int main() {
	int test; cin >> test;
	for (int num = 1; num <= test; num++) {
		int n, a[N] = {};
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		int ans = *max_element(a, a + n);
		for (int nor = 1; nor < N; nor++) {
			int tmp = 0;
			for (int i = 0; i < n; i++)
				tmp += (a[i] - 1) / nor;
			ans = min(ans, tmp + nor);
		}
		cout << "Case #" << num << ": ";
		cout << ans << '\n';
	}
	return 0;
}
