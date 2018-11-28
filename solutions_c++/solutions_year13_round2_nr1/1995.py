#include <iostream>
#include <algorithm>

using namespace std;


#define N 105
long long b[N], a, n;

long long solve(int s, int a) {
	if (s >= n)
		return 0;
	else if (b[s] < a) {
		a += b[s];
		return solve(s + 1, a);

	} else if (a == 1) {
		return 1 + solve(s + 1, a);
	} else {
		long long tempa = a, cnta = 0;
		while (tempa <= b[s]) {
			tempa += (tempa - 1);
			cnta++;
		}
		cnta += solve(s, tempa);

		long long cntb = 1 + solve(s + 1, a);
		return min(cnta, cntb);
	}
}

int main() {

	int tc;
	cin >> tc;

	for (int t = 1; t <= tc; ++t) {
		cin >> a >> n;
		for (int i = 0; i < n; ++i)
			cin >> b[i];
		sort(b, b + n);
		long long res = solve(0, a);
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
