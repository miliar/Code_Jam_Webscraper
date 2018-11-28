#include "template.h"

int exist[10] = { 0,0,0,0,0, 0,0,0,0,0 };

void countIt(long long x) {
	while (x >= 0) {
		exist[x % 10] = 1;
		x /= 10;

		if (x == 0) {
			return;
		}
	}
}

int main() {
	cin.sync_with_stdio(false);

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		long long n;
		cin >> n;

		memset(exist, 0, sizeof(exist));

		long long ans = -1;
		long long x = n;

		for (int i = 1; i < 10000000; ++i) {
			//if (i % 100000 == 0) cout << tc << " - iterating " << i << endl;

			countIt(x);

			if ( find(exist, exist + 10, 0) == (exist + 10) ) {
				ans = i * n;
				break;
			}
			x += n;
		}

		if (ans == -1) {
			//for (int k : exist) {cout << k << " - ";}cout << endl;
			cout << "Case #" << tc << ": INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << tc << ": " << ans << endl;
		}
	}
	return 0;
}