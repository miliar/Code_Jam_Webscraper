#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	unsigned int T;
	unsigned int A, B, K;

	unsigned int i, j, l;

	cin >> T;
	for (i = 1; i <= T; i++) {
		cin >> A >> B >> K;
		int count = 0;
		for (j = 0; j < A; j++) {
			for (l = 0; l < B; l++) {
				if ((j & l) < K ) {
					count++;
				}
			}
		}
		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}
