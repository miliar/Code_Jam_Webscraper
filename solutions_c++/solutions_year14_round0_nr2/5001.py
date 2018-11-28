//In the name of God
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int test;
	cin >> test;
	cout << fixed << setprecision(7);
	for (int i = 1; i <= test; i++) {
		long double c, f, x, t = 0;
		cin >> c >> f >> x;
		long double ans = x / 2, m = 2;
		while (true) {
			t += c / m;
			m += f;
			if (ans > t + x / m)
				ans = t + x / m;
			else
				break;
		}
		cout << "Case #" << i << ": " << ans << '\n';
	}
	return 0;
}
