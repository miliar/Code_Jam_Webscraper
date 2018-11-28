#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <cstdio>
#include <limits>
#define _USE_MATH_DEFINES
#define vi vector<int>
using namespace std;
int main () {
	freopen ("D:\\Internet\\A-large.in", "r", stdin);
	freopen ("A-output-large.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		cout << "Case #" << t << ": ";
		if (n == 0) {
			cout << "INSOMNIA\n";
			continue;
		}
		bool d [10];
		memset (d, 0, sizeof(d));
		int p = n, ans = n, count = 0;
		for (int p = n; count < 10; p += n) {
			ans = p;
			while (p > 0) {
				if (!d[p % 10]) {
					d[p % 10] = true;
					count++;
				}
				if (count == 10)
					break;
				p = p / 10;
			}
			p = ans;
		}
		cout << ans << endl;
	}
}