#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

const int INF = 1e9;

int flipPancakes(string pancakes, int k) {
	int flips = 0;
	for (int i = 0; i + k <= pancakes.length(); i++) {
		if (pancakes[i] == '-') {
			flips++;
			for (int j = i; j < i + k; j++) {
				if (pancakes[j] == '-') {
					pancakes[j] = '+';
				}
				else {
					pancakes[j] = '-';
				}
			}
		}
	}
	for (int i = 0; i < pancakes.length(); i++) {
		if (pancakes[i] == '-') {
			return INF;
		}
	}
	return flips;
}

void solve() {
	string pancakes;
	int k;
	cin >> pancakes >> k;

	int minFlips = flipPancakes(pancakes, k);
	reverse(pancakes.begin(), pancakes.end());
	minFlips = min(minFlips, flipPancakes(pancakes, k));

	if (minFlips == INF) {
		cout << "IMPOSSIBLE";
	}
	else {
		cout << minFlips;
	}
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
