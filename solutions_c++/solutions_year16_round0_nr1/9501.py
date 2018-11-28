#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>

using namespace std;

int main() {
	int T; // number of tests
	scanf("%d", &T);

	vector<int> result;

	for (int i = 0; i < T; i++) {
		int N;
		scanf("%d", &N);

		if (N == 0) {
			result.push_back(-1);
			continue;
		}

		bool hasSeen[10] = { false };
		int digitsCount = 0;

		int count = 0;
		while (true) {
			count++;
			int currentNumber = N * count;
			int x = currentNumber;
			while (true) {
				int y = x%10;
				x = x/10;
				if (!hasSeen[y]) {
					digitsCount++;
					hasSeen[y] = true;
				}
				if (x == 0) {
					break;
				}
			}
			if (digitsCount == 10) {
				result.push_back(currentNumber);
				break;
			}
		}
	}

	for (int i = 0; i < T; i++) {
		if (result[i] == -1) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << result[i] << endl;
		}
	}
}
