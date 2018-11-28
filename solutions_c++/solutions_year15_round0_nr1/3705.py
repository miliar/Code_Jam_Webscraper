#include <iostream>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		int smax;
		cin >> smax;
		string S;
		cin >> S;
		int toInvite = 0, standing = S[0] - '0';
		for (int i = 1; i <= smax; ++i) {
			int k = S[i] - '0';
			if (k > 0) {
				if (standing >= i) {
					standing += k;
				} else {
					toInvite += i - standing;
					standing = i + k;
				}
			}
		}
		cout << "Case #" << test << ": " << toInvite << endl;
	}
	return 0;
}
