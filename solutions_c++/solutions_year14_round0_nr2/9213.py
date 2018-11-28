#include<iostream>
#include<iomanip>
using namespace std;
int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("outtpu.in", "w", stdout);
	int t;
	cin >> t;
	for (int t1 = 1; t1 <= t; t1++) {
		double c, f, x;
		cin >> c >> f >> x;
		double ans = 0.0;
		double r = 2.0;
		for (; (x / r) > (c / r + (x) / (r + f));) {
			ans += (c / r);
			r += f;
		}
		ans += (x / r);
		cout << "Case #" << t1 << ": ";
		cout << setprecision(7) << fixed << ans << "\n";
	}
	return 0;
}
