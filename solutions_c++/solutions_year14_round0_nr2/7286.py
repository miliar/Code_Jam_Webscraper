#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	freopen("problemB.in", "r", stdin);
	freopen("problemB.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		double c, f, x;
		cin >> c >> f >> x;
		long long n = (long long)floor(x / c - 2 / f);
		if (n < 0) n = 0;
		double farmTime = 0.5;
		for (int j = 1; j < n; j++) {
			farmTime += 1.0 / (2 + f*j);
		}
		double goalTime = x / (2.0 + f*n);
		double result = n == 0 ? goalTime : c*farmTime + goalTime;
		cout << "Case #" << i + 1 << ": ";
		cout.precision(14);
		cout << fixed << result << "\n";
	}

	cout.flush();
	fclose(stdin);
	fclose(stdout);
	return 0;
}
