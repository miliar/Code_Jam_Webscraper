#include <iostream>
using namespace std;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t + 1 << ':' << ' ';
		long double c, f, x;
		cin >> c >> f >> x;
		long double min_ = x / 2;
		long double ans;
		int cnt = 1;
		long double px = c / 2;
		long double speed = 2 + f;
		ans = min_;
		do {
			min_ = ans;
			ans = px + x / speed;
			px += c / speed;
			speed += f;
			++cnt;
		}
		while (ans < min_);
		printf("%.10llf\n", min_);
	}
}