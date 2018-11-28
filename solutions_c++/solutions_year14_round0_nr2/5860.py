#include<iostream>
using namespace std;

int main() {
	int n;
	double c, f, x, rate, t, s, ans;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> c >> f >> x;
		t = c/f;
		s = 0;
		rate = 2;
		ans = 0;
		if (c < x) {
			while (s < x) {
				s += c;
				ans += c/rate;
				if (s + rate*t < x) {
					s -= c;
					rate += f;
				}
				else {
					ans += (x-s)/rate;
					s = x;
				}
			}
		}
		else {
			ans = x / rate;
		}
		printf("Case #%d: %f\n", i+1, ans);
	}
	return 0;
}