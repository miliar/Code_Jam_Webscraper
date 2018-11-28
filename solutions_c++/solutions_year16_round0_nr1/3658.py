//============================================================================
// Name        : q1a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	unsigned int T, N, sum;
	int i, j;
	bool seen[10];
	int seenCount;
	string sn;

	cin >> T;
	for (i = 0; i < T; i++) {
		cin >> N;
		if (N != 0) {
			for (j = 0; j < 10; j++) {
				seen[j] = false;
			}
			seenCount = 0;
			sum = 0;
			while (seenCount < 10) {
				sum += N;
				sn = to_string(sum);
				for (j = 0; j < sn.size(); j++) {
					if (!seen[sn[j] - '0']) {
						seen[sn[j] - '0'] = true;
						seenCount++;
					}
				}
			}
			cout << "Case #" << i+1 << ": " << sum << endl;
		} else {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
	}
	return 0;
}
