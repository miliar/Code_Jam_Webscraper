#include <iostream>
using namespace std;

int main (void) {
	int nb;
	cin >> nb;
	for (int c = 0; c < nb; ++c) {
		int smax;
		cin >> smax;

		int standing = 0;
		int shyness = 0;
		int nb_friend = 0;

		for (int shyness = 0; shyness <= smax; ++shyness) {
			if (shyness > standing) {
				int needed = shyness - standing;
				nb_friend += needed;
				standing = shyness;
			}

			char n;
			cin >> n;
			standing += n - '0';
		}

		cout << "Case #" << c + 1 << ": " << nb_friend << endl;
	}
}
