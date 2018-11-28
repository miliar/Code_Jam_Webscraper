//============================================================================
// Name        : r1a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	int T, N;
	int plate[2000];
	int i, j, m1, m2;
	int rate;

	cin >> T;

	for (i = 0; i < T; i++) {
		cin >> N;
		for (j = 0; j < N; j++) {
			cin >> plate[j];
		}

		// Determine rate
		rate = 0;
		for (j = 1; j < N; j++) {
			rate = max(rate, plate[j - 1] - plate[j]);
		}

		m1 = 0;
		m2 = 0;
		for (j = 1; j < N; j++) {
			if (plate[j] < plate[j-1]) {
				m1 += plate[j-1] - plate[j];
			}
			m2 += min(plate[j - 1], rate);
		}
		cout << "Case #" << i + 1 << ": " << m1 << " " << m2 << endl;
	}

	return 0;
}
