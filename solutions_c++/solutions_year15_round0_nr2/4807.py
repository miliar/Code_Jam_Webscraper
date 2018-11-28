#include <iostream>
#include <cstring>

#define MAXD 1001
using namespace std;

int T, D, count_p[MAXD], max_p, result;
int f[MAXD];

int c = 0;

void solve(int x) {
	if (count_p[x] > 0) {
		if (x + c < result) {
			result = x + c;
		}
		if (x < 4) {
			return;
		}
		c += count_p[x];
		for (int i = x / 2; i > 0; --i) {
			count_p[x - i] += count_p[x];
			count_p[i] += count_p[x];
			solve(x - 1);
			count_p[x - i] -= count_p[x];
			count_p[i] -= count_p[x];
		}
		c -= count_p[x];
	} else {
		if (x == 0) {
			return;
		}
		solve(x - 1);
	}
}

int main() {
	cin >> T;
	int p;
	for (int t = 1; t <= T; ++t) {
		result = MAXD;
		c = 0;
		memset(count_p, 0, sizeof(int) * MAXD);
		max_p = 0;
		cin >> D;
		for (int i = 0; i < D; ++i) {
			cin >> p;
			if (p > max_p) {
				max_p = p;
			}
			++count_p[p];
		}
		solve(max_p);
		cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}