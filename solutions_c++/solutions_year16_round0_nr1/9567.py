#include <iostream>
using namespace std;
#define N 1000001

int solve(int n) {
	int r = 1;
	long long d = 0, x;
	bool a[10] = { 0 };

	while (1) {
		x = n*r;	
		do {
			if (!a[x % 10]) {
				a[x % 10] = 1;
				d++;
			}

			x /= 10;
		} while (x > 0);
 
		if (d == 10)
			return n*r;

		r++;
	}
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n;
		cin >> n;

		if (!n)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else	
			cout << "Case #" << t << ": " << solve(n) << endl;
	}
}