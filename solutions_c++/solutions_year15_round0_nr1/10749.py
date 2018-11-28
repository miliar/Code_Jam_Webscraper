#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; i++) {
		int max, input;
		cin >> max;
		cin >> input;
		int S[max+1];
		for (int j = 0; j < max+1; j++) {
			S[max+1-j-1] = input/(int)pow(10,j) % 10;
		}
		int need = 0;
		int have = 0;
		for (int j = 0; j <= max; j++) {
			int sumBefore = 0;
			if (j >= have) {
				need += j - have;
				have += j - have;
			}
			have += S[j];
		}
		cout << "Case #" << i+1 << ": " << need << endl;
	}
}
