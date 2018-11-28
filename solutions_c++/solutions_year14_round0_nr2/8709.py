#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	ofstream cout("test.out");
	ifstream cin("A-small-practice.in");
	double c, f, x, rate;
	cin >> c;
	for (int u = 0; cin >> c >> f >> x; ++u) {
		rate = 2;
		cout << "Case #" << u << ": ";
		long double curr = 0, tm = x / rate;
		for (long double i = 0; curr < tm; ++i)
			curr += c / (rate + f * i), tm = min(tm,
					curr + x / (rate + f * (i + 1)));
		cout << fixed << tm << endl;
	}
}
