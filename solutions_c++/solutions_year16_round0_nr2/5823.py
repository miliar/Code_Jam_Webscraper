#include <sstream>
#include <iostream>
#include <stdio.h>

using namespace std;

int flipPancakes(string s) {
	int numFlips = 0;
	for (int i = s.size() - 1; i >= 0; --i) {
		if ((s[i] == '+' && !(numFlips % 2)) || (s[i] == '-' && (numFlips % 2)))
			continue;
		numFlips++;
	}
	return numFlips;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	int T;
	string pancakesStack;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		cin >> pancakesStack;
		int sol = flipPancakes(pancakesStack);
		printf("Case #%d: %d\n", t + 1, sol);
	}
	return 0;
}
