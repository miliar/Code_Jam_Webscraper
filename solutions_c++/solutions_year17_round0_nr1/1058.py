//============================================================================
// Name        : A_Pancake.cpp
// Author      : Oliver Roese
//============================================================================

#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

void flipAt(string& cake, unsigned K, unsigned i) {
	for (unsigned j = i; j< i+K; ++j) {
		const char c = cake[j];
		cake[j] = (c == '-') ? '+' : '-';
	}
}

int getFlipCount(string& cake, unsigned K) {
	assert(2<=K && K<=cake.length());

	int flips = 0;
	for (unsigned i = 0; i <= cake.length()-K; ++i) {
		assert(cake[i] == '+' || cake[i] == '-');

		if (cake[i] == '-') {
			flipAt(cake, K, i);
			++flips;
		}
	}
	if (find(cake.end()-K, cake.end(), '-') != cake.end()) {
		flips = -1;
	}


	return flips;
}

void writeResult(unsigned caseNr, int flips) {
	printf("Case #%d: ", caseNr);
	if (flips < 0) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%d\n", flips);
	}

}

void processCakeStrings() {
	unsigned T = 0;
	cin >> T;
	assert(T>0);
	for (unsigned caseNr = 1; caseNr <= T; ++caseNr) {
		string currentCake;
		unsigned K;

		cin >> currentCake >> K;

		const int flips = getFlipCount(currentCake,K);
		writeResult(caseNr,flips);
	}
}

int main() {
	processCakeStrings();
	return 0;
}
