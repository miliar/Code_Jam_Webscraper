#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main() {
	int T, N;
	int i, j, k, l;
	char c;
	string s[100];
	int current[100];
	int repeat[100][100];

	cin >> T;
	for (i=1; i<=T; i++) {
		cin >> N;
		for (j = 0; j < N; j++) {
			cin >> s[j];
		}
		for (j = 0; j < N; j++) {
			current[j] = 0;
		}

		bool more;
		bool valid = true;
		int index = 0;
		do {
			more = false;
			if (current[0] >= s[0].length()) {
				valid = false;
				break;
			}
			c = s[0][current[0]];
			for (j = 0; j < N; j++) {
				int count = 0;
				for (k = current[j]; k < s[j].length() && s[j][k] == c; k++) {
					count++;
				}
				if (count == 0) {
					valid = false;
					break;
				}
				repeat[j][index] = count;
				current[j] = k;
				if (current[j] < s[j].length()) {
					more = true;
				}
			}
			index++;
		}
		while (valid && more);

		if (valid) {
			int total = 0;
			for (j = 0; j < index; j++) {
				int minChange = 1000;
				for (k = 0; k < N; k++) {
					int f = repeat[k][j];
					int changeCount = 0;
					for (l = 0; l < N; l++) {
						if (repeat[l][j] != f) {
							changeCount += abs(repeat[l][j] - f);
						}
					}
					if (changeCount < minChange) {
						minChange = changeCount;
					}
				}
				total += minChange;
			}
			cout << "Case #" << i << ": " << total << endl;
		}
		else {
			cout << "Case #" << i << ": Fegla Won" << endl;
		}
	}
	return 0;
}
