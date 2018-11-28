#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	cout << fixed;
	cout.precision(9);
	for (int t=1; t<=T; t++) {
		int N;
		double A, B;
		double a, b, c, d;
		cin >> N >> A >> B;
		if (N == 1) {
			cin >> a >> b;
			cout << "Case #" << t << ": ";
			if (abs(b - B) < 1e-9) {
				cout << A / a << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		} else {
			cin >> a >> b >> c >> d;
			cout << "Case #" << t << ": ";
			if (abs(b - d) < 1e-9) {
				if (abs(b - B) < 1e-9) {
					cout << A / (a+c) << endl;
				} else {
					cout << "IMPOSSIBLE" << endl;
				}
			} else {
				double x = A * (B - d) / a / (b - d);
				double y = A * (B - b) / c / (d - b);
				if (b + 1e-9 < B && d + 1e-9 < B) {
					cout << "IMPOSSIBLE" << endl;
				} else if (b > B + 1e-9 && d > B + 1e-9) {
					cout << "IMPOSSIBLE" << endl;
				} else {
					cout << max(x, y) << endl;
				}
			}
		}
	}
	return 0;
}
