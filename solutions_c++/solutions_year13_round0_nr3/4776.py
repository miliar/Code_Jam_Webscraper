#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

int digits[100];

bool test(int n) {
	int div = n;
	int rem = 0;
	int count = 0;

	while (div != 0 && count < 100) {
		rem = div % 10;
		div = div / 10;
		digits[count] = rem;
		count++;
	}
	int half = count / 2;
	for (int i = 0; i < half; ++i) {
		if (digits[i] != digits[count - (i + 1)])
			return false;
	}
	return true;
}

int main(int argc, char **argv) {
	int testCount = 0;
	cin >> testCount;
	int min;
	int max;
//	test(1234324321);
//	return 0;

	for (int i = 0; i < testCount; ++i) {
		cin >> min;
		cin >> max;
		int count = 0;
		for (int j = min; j <= max; ++j) {
			int root = (int) sqrt(j);
			if (root * root == j) {
				if (test(j) && test(root)) {
					count++;
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << count << endl;
	}
}
