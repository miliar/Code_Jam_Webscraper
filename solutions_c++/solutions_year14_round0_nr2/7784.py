#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int T;
	double c, f, x;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> c >> f >> x;
		int buyTime = ceil(((x - c) / c * f - 2) / f);
		if (buyTime < 0)
			buyTime = 0;
		double ans = 0;

		for (int j = 0; j < buyTime; ++j)
			ans += c / (2 + j*f);
		ans += x / (2 + buyTime*f);
		cout << "Case #" << i << ": ";
		cout << fixed << setprecision(7) << ans << endl;
	}

	return 0;
}