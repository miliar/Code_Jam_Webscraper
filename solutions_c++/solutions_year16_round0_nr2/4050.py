#include <cstdio>
#include <iostream>
#include <string>
#include <cassert>
using namespace std;

int minFlips(string S) {
	int n = S.size();
	assert(n > 0);
	int flips = (S[n - 1] == '-');
	for (int i = n - 2; i >= 0; i--) {
		if (S[i] != S[i+1])
			flips++;
	}
	return flips;
}

int main(void) {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	string S;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> S;
		cout << "Case #" << t << ": " << minFlips(S) << '\n';
	}
	return 0;
}
