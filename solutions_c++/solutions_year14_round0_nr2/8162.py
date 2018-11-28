#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t, idx = 1;
	double c, f, x, tmp, res, st, sum;
	cin >> t;
	while(t--) {
		res = 1.0 / 0.0;
		sum = 0.0, st = 2.0;
		cin >> c >> f >> x;
		while(true) {
			tmp = x / st + sum;
			if(tmp > res) break;
			res = tmp, sum += c / st, st += f;
		}
		printf("Case #%d: %.6f\n", idx++, res);
	}

	return 0;
}
