//============================================================================
// Name        : gcj-fs.cpp
// Author      : Yo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>
using namespace std;

unsigned int b = 10;

bool fair(unsigned int i) {
	unsigned int r, R, j = 1;

	while (j < i)
		j *= b;

	while (j >= b) {
		j /= b;

		r = i % b;
		if (i >= j) {
			R = i / j;

			if (R > 0 && R != r)
				return false;

			i = (i % (j * R)) / b;
		}
	}

	return true;
}

bool fs(unsigned int i) {
	unsigned int sqr = sqrt(i);

	if (sqr * sqr != i)
		return false;

	return fair(sqr) && fair(i);
}

unsigned int countfs(unsigned int start, unsigned int end) {
	unsigned int count = 0;

	for (unsigned int i = start; i <= end; i++) {
		count += fs(i) * 1;
	}

	return count;
}

int main() {
	unsigned int n, s, e;

	if (cin >> n) {
		for (unsigned int i = 0; i < n; i++) {
			cin >> s;
			cin >> e;

			cout << "Case #" << (i+1) << ": " << countfs(s, e) << endl;
		}
	}

	return 0;
}
