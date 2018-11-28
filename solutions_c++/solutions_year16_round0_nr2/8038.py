#include <bits/stdc++.h>
#define LOG(x) // cout << #x << " is " << x << endl;
using namespace std;

bool any(int* str, int len, int val) {
	for (int i = 0; i < len; i++) {
		if (str[i] == val) {
			return true;
		}
	}
	return false;
}

bool minusPlus(int* str, int len) {
	bool plus = false;
	if (str[0] != 0) {
		return false;
	}
	for (int i = 0; i < len; i++) {
		if (str[i] == 1) {
			if (plus) {
				continue;
			} else {
				plus = true;
			}
		} else {
			if (!plus) {
				continue;
			} else {
				return false;
			}
		}
	}
	return true;
}

bool plusMinus(int* str, int len) {
	bool minus = false;
	if (str[0] != 1) {
		return false;
	}
	for (int i = 0; i < len; i++) {
		if (str[i] == 1) {
			if (!minus) {
				continue;
			} else {
				return false;
			}
		} else {
			if (minus) {
				continue;
			} else {
				minus = true;
			}
		}
	}
	return true;
}

int* flip(int* str, int l, int r) {
	if (l == r || l == r - 1) {
		return str;
	}
	int len = r - l;
	int idx;
	if (len % 2 != 0) {
		idx = l + ceil((float)len/2.0f) - 1;
		str[idx] = str[idx] ^ 1;
	} else {
		idx = l + len/2;
	}

	for (int i = l; i < idx; i++) {
		int tmp = str[i];
		str[i] = str[r - i - 1] ^ 1;
		str[r - i - 1] = tmp ^ 1;
	}

	return str;
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	// int z[] = {1, 0, 1, 1, 0, 1, 0};

	// for (int i = 0; i < 7; i++) {
	// 	cout << z[i];
	// }
	// cout << endl;

	// flip(z, 0, 7);
	// for (int i = 0; i < 7; i++) {
	// 	cout << z[i];
	// }
	// cout << endl;
	// flush(cout);
	// return 0;

	/*
	+-++--+++-
	--++--+++-
	++++--+++-
	------+++-
	+++++++++-
	----------
	++++++++++

	+-+-
	--+-
	+++-
	----
	++++

	+++-+++--+
	----+++--+
	+++++++--+
	---------+
	++++++++++
	*/

	int cases;
	cin >> cases;

	int n;

	for (int i = 0; i < cases; i++) {
		string p = "";
		cin >> p;

		int* str = new int[p.length()];
		for (int i = 0; i < p.length(); i++) {
			str[i] = (p[i] == '+' ? 1 : 0);
		}

		int flips = 0;

		while (true) {
			if (!any(str, p.length(), 0) || !any(str, p.length(), 1)) {
				if (str[0] == 0) {
					cout << "Case #" << i+1 << ": " << flips + 1 << '\n';
				} else {
					cout << "Case #" << i+1 << ": " << flips << '\n';
				}
				break;
			} else if (plusMinus(str, p.length())) {
				cout << "Case #" << i+1 << ": " << flips + 2 << '\n';
				break;
			} else if (minusPlus(str, p.length())) {
				cout << "Case #" << i+1 << ": " << flips + 1 << '\n';
				break;
			} else {
				int val = str[0];
				int runs = 1	;
				for (int j = 1; j < p.length(); j++) {
					if (str[j] != val) {
						runs++;
						val = str[j];
					}
				}

				if (str[p.length() - 1] == 1) {
					runs--;
				}
				cout << "Case #" << i+1 << ": " << runs << '\n';
				break;
			}
		}

		// while (any(str, p.length())) {
		// 	int r = p.length() - 1;
		// 	int val = str[r];
		// 	while (str[r] == val) {
		// 		r--;
		// 	}
		// 	val = str[r];
		// 	while (str[0] == val || str[0]) {

		// 	}
		// }

		// -+-+
		// ++-+
		// ---+
		// ++++

		// +-+-
		// --+-
		// +++-
		// -+++
		// ++++

		// +-+-+--
		// --+-+--
		// +++-+--
		// ----+--
		// +++++--
		// -----++
		// +++++--

		// +-+++++-++
		// --+++++-++
		// +++++++-++
		// --------++
		// ++++++++++

		// +-+++++-++
		// --+++++-++
		// +-----++++
		// ------++++
		// ++++++++++
	}


	return 0;
}