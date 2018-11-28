#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>

#define LL long long
#define LD long double

using namespace std;
LL T;
LD s, c, f, x;
LD tmin, sum;

int main() {
	freopen("ex.in", "r", stdin);
	freopen("ex.out", "w", stdout);

	cin >> T;
	s = 2;
	for (int it = 0; it < T; it++) {
		cin >> c >> f >> x;
		tmin = x / s;
		sum = 0;
		for (int n = 0; n < 100000; n++) {
            sum += c / (s + n * f);
            if (sum + x / (s + f + n * f) < tmin) tmin = sum + x / (s + f + n * f);
		}
/*		n = x / c - s / f - 2;
*/		cout << "Case #" << it + 1 << ": ";
		printf("%0.7f\n", (float)tmin);


	}
	return 0;
}
