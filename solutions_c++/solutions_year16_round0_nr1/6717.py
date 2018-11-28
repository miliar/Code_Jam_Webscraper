#include <iostream>
#include <vector>
#include <string>
 
using namespace std;
 
int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	long long t, T, i, c, n, ans, p;
	cin >> T;
 
	for (t = 0; t < T; ++t) {
		int d[10] = { 0 };
		p = 0;
		i = 0;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
		}
		else {
			while (true) {
				i++;
				ans = i * n;
				c = ans;
				while (c > 0) {
					if (!d[c % 10]) {
						d[c % 10]++;
						p++;
					}
					c = c / 10;
				}
				if (p == 10) break;
			}
			cout << "Case #" << t + 1 << ": " << ans << endl;
		}
	}
	return 0;
}