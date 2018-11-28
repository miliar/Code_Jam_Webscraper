//============================================================================
// Name        : 1a-b.cpp
// Author      : Long Pham
// Version     :
// Copyright   : 
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

	cin >> T;
	int counter[3000];
	int x;
	const int maxH = 2500;

	for (int t = 0; t < T; t++) {
		cin >> N;
		for (int i=1; i<= maxH; i++) {
			counter[i] = 0;
		}

		for (int i = 0; i < 2*N-1; i++) {
			for (int j = 0; j < N; j++) {
				cin >> x;
				counter[x]++;
			}
		}

		cout << " Case #" << t+1 << ":";
		int found = 0;
		for (int i=1; i<= maxH && found < N; i++) {
			if (counter[i] % 2 != 0) {
				cout << " " << i;
				found++;
			}
		}

		cout << endl;
	}
	return 0;
}
