#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int c[1001];
int big;

int solve() {
	int best = big, mov = 0;
	for (int i = 1; i <= big; i++) {
		// calc splits needed to get here!
		int divs = 0;
		for (int j = i + 1; j <= big; j++) {
			divs += c[j] * (j / i - !(j % i));
		}
		// cerr << "score for " << i << " : " << i + divs << endl;
		best = min(i + divs, best);
	}
	return best;
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t++ < T;) {
		int D, P;
		memset(c, 0, sizeof(c));
		cin >> D;
		big = 0;
		while (D--) {
			cin >> P;
			c[P]++;
			if (P > big) big = P;
		}
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}