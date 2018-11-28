#include <iostream>

using namespace std;

int main() {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; ++i) {
		int maxsh;
		cin >> maxsh;

		string lev;
		cin >> lev;

		int invitees = 0;

		int standing = 0;

		standing += lev[0] - '0';

		for (int j = 1; j <= maxsh; ++j) {
			char elc = lev[j];
			int el = elc - '0';
			//cout << el;
			//cout << "standing: " << standing;
			//cout << "shyness: " << j << endl;
			if (standing < j) {
				invitees += j - standing;
				standing += j - standing;
			}
			standing += el;
		}
		cout << "Case #" << i + 1 << ": " << invitees << endl;
	}

	return 0;
}
