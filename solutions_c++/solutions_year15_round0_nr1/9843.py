#include <iostream>

using namespace std;
int main() {
	int tests;
	cin >> tests;

	for (int i = 1; i <= tests; ++i) {
		// minimum number of invitations required and number of people already clapping
		int invites {}, clapping {};
		char c;
		cin >> c;
		int max = c - '0';
		for (int required_clapping = 0; required_clapping < max + 1; ++required_clapping) {
			cin >> c;
			// need to invite some friends
			if (required_clapping > clapping) {
				invites += required_clapping - clapping;
				clapping = required_clapping;
			}
			clapping += c - '0';
		}

		cout << "Case #" << i << ": " << invites << endl;

	}
}