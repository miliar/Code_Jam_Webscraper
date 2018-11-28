//============================================================================
// Name        : q1b.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>

using namespace std;

const int MAX_P = 2000;

int main() {
	int T, D;
	int cost, maxHeight, cutoff;
	int i, j;
	int moves;
	double r;

	cin >> T;

	int P[MAX_P];

	for (i = 0; i < T; i++) {
		cin >> D;
		maxHeight = 0;
		for (j = 0; j < D; j++) {
			cin >> P[j];
			if (maxHeight < P[j]) {
				maxHeight = P[j];
			}
		}

		// Solve P
		cost = maxHeight;
		for (cutoff = 1; cutoff < maxHeight; cutoff++) {
			moves = 0;
			for (j = 0; j < D; j++) {
				if (P[j] > cutoff) {
					r = P[j] - cutoff;
					moves += (int) ceil(r/cutoff);
				}
			}
			if (cutoff + moves < cost) {
				cost = cutoff + moves;
			}
		}

		cout << "Case #" << i + 1 << ": " << cost << endl;
	}
	return 0;
}
