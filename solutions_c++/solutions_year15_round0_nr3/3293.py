#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int mul_table [5][5];

int sgn(int k1, int k2) {
	return (k1 * k2 < 0 ? -1 : 1);
}

int mul(int k1, int k2) {
	/*if (k1 == 0 || k2 == 0 || abs(k1) > 4 || abs(k2) > 4) {
		cout << "???";
	}*/
	if (abs(k1) == 1 || abs(k2) == 1) {
		return k1 * k2;
	}

	return sgn(k1, k2) * mul_table[abs(k1)][abs(k2)];
}

int main() {
	ifstream test_file ("C-small-attempt3.in", ios::in);
	ofstream output;
	output.open("C-small-attempt3.out");
	int t, l, x;
	test_file >> t;

	// ------table------
	mul_table[2][2] = -1;
	mul_table[3][3] = -1;
	mul_table[4][4] = -1;

	mul_table[2][3] = 4;
	mul_table[2][4] = -3;
	mul_table[3][2] = -4;
	mul_table[3][4] = 2;
	mul_table[4][2] = 3;
	mul_table[4][3] = -2;
	// -----------------

	int* symbols;
	for (int testNum = 0; testNum < t; testNum++) {
		test_file >> l >> x;
		symbols = new int[l * x + 1];
		int total = 1;
		for (int i = 0; i < l; i++) {
			char c;
			test_file >> c;
			symbols[i] = (c - 'i') + 2;
			total = mul(total, symbols[i]);
		}

		
		bool fits = false;
		int full = total;
		for (int i = 1; i < x; i++) {
			full = mul(full, total);
		}
		if (full == -1) {
			fits = true;
		}
		/*if (total == -1 && x % 2 == 1) {
			fits = true;
		}
		if (abs(total) > 0 && (x % 2 == 0) && ((x / 2) % 2 == 1)) {
			fits = true;
		}*/
		if (!fits) {
			output << "Case #" << (testNum + 1) << ": " << "NO" << endl;
			continue;
		}

		// copy
		for (int i = 1; i < x; i++) {
			int offset = l * i;
			for (int j = 0; j < l; j++) {
				symbols[offset + j] = symbols[j];
			}
		}

		//check i
		int i_index = -1;
		int current = 1;
		for (int i = 0; i < x * l; i++) {
			current = mul(current, symbols[i]);
			if (current == 2) {
				i_index = i;
				break;
			}
		}

		// check k
		int j_index = -1;
		current = 1;
		for (int i = x * l - 1; i >= 0; i--) {
			current = mul(symbols[i], current);
			if (current == 4) {
				j_index = i;
				break;
			}
		}

		bool possible = false;
		if (i_index >= 0 && j_index > 0 && (i_index < j_index - 1)) {
			possible = true;
		}
		output << "Case #" << (testNum + 1) << ": " << (possible ? "YES" : "NO") << endl;
	}

	return 0;
}