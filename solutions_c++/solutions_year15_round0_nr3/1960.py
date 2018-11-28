#include <iostream>
#include <vector>
using namespace std;

typedef char quat;
#define U 1
#define I 2
#define J 3
#define K 4


static quat quat_mul (quat a, quat b) {
	static quat table[4][4] = {
		{ U, I, J, K },
		{ I, -U, K, -J },
		{ J, -K, -U, I },
		{ K, J, -I, -U }
	};
	char f = 1;
	if (a < 0) { a = -a; f = -f; }
	if (b < 0) { b = -b; f = -f; }
	return f * table[a - 1][b - 1];
}

int main (void) {
	int nb_case; cin >> nb_case;
	for (int c = 0; c < nb_case; c++) {
		// load case
		int l, x; cin >> l >> x;
		vector<quat> chain (l, 0);	
		
		for (int i = 0; i < l; i++) {
			char q; cin >> q;
			switch (q) {
				case '1': chain[i] = U; break;
				case 'i': chain[i] = I; break;
				case 'j': chain[i] = J; break;
				case 'k': chain[i] = K; break;
			}
		}

		if (x > 12)
			x = 12 + x % 4; // q^4 == 1, so only check for x in 1..3

		int pos = 0;
		int bound = l * x;
		quat acc = U;
		
		// find i
		for (; pos < bound && acc != I; ++pos)
			acc = quat_mul (acc, chain[pos % l]);

		if (acc == I) {
			// find J
			acc = U;
			for (; pos < bound && acc != J; ++pos)
				acc = quat_mul (acc, chain[pos % l]);

			if (acc == J) {
				// check ends with K
				acc = U;
				for (; pos < bound; ++pos)
					acc = quat_mul (acc, chain[pos % l]);

				if (acc == K) {
					cout << "Case #" << c + 1 << ": YES" << endl;
					continue;
				}
			}

		}

		cout << "Case #" << c + 1 << ": NO" << endl;
	}

	return 0;
}

