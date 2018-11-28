#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

struct Quat {
	char value;
	int symbol;
};

Quat mult(Quat a, Quat b) {
	Quat c;
	if (a.value == 'i') {
		if (b.value == 'i') {
			c.value = '1';
			c.symbol = a.symbol * b.symbol * (-1);
		}
		else if (b.value == 'j') {
			c.value = 'k';
			c.symbol = a.symbol * b.symbol;
		}
		else if (b.value == 'k') {
			c.value = 'j';
			c.symbol = a.symbol * b.symbol * (-1);
		}
		else if (b.value == '1') {
			c.value = 'i';
			c.symbol = a.symbol * b.symbol;
		}
	}
	else if (a.value == 'j') {
		if (b.value == 'i') {
			c.value = 'k';
			c.symbol = a.symbol * b.symbol * (-1);
		}
		else if (b.value == 'j') {
			c.value = '1';
			c.symbol = a.symbol * b.symbol * (-1);
		}
		else if (b.value == 'k') {
			c.value = 'i';
			c.symbol = a.symbol * b.symbol;
		}
		else if (b.value == '1') {
			c.value = 'j';
			c.symbol = a.symbol * b.symbol;
		}
	}
	else if (a.value == 'k') {
		if (b.value == 'i') {
			c.value = 'j';
			c.symbol = a.symbol * b.symbol;
		}
		else if (b.value == 'j') {
			c.value = 'i';
			c.symbol = a.symbol * b.symbol * (-1);
		}
		else if (b.value == 'k') {
			c.value = '1';
			c.symbol = a.symbol * b.symbol * (-1);
		}
		else if (b.value == '1') {
			c.value = 'k';
			c.symbol = a.symbol * b.symbol;
		}
	}
	else if (a.value == '1') {
		if (b.value == 'i') {
			c.value = 'i';
			c.symbol = a.symbol * b.symbol;
		}
		else if (b.value == 'j') {
			c.value = 'j';
			c.symbol = a.symbol * b.symbol;
		}
		else if (b.value == 'k') {
			c.value = 'k';
			c.symbol = a.symbol * b.symbol;
		}
		else if (b.value == '1') {
			c.value = '1';
			c.symbol = a.symbol * b.symbol;
		}
	}
	return c;
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int zz = 1; zz <= t; zz++) {

		string data;
		long long n, m;
		cin >> n >> m;
		long long all = n * m;
		cin >> data;
		Quat start;
		start.value = '1';
		start.symbol = 1;
		long long total = 0;
		long long curr = 0;
		bool found = false;
		while (total < 4 * n && curr < all) {
			Quat current;
			current.value = data[curr % n];
			current.symbol = 1;
			start = mult(start, current);
			total++;
			curr++;
			if (start.value == 'i' && start.symbol == 1) {
				found = true;
				break;
			}
		}

		if (!found) {
			cout << "Case #" << zz << ": NO\n";
			continue;
		}

		start.value = '1';
		found = false;
		total = 0;
		while (total < 4 * n && curr < all) {
			Quat current;
			current.value = data[curr % n];
			current.symbol = 1;
			start = mult(start, current);
			total++;
			curr++;
			if (start.value == 'j' && start.symbol == 1) {
				found = true;
				break;
			}
		}

		if (!found) {
			cout << "Case #" << zz << ": NO\n";
			continue;
		}

		start.value = '1';
		found = false;
		total = 0;
		while (total < 4 * n && curr < all) {
			Quat current;
			current.value = data[curr % n];
			current.symbol = 1;
			start = mult(start, current);
			total++;
			curr++;
			if (start.value == 'k' && start.symbol == 1) {
				found = true;
				break;
			}
		}

		if (!found) {
			cout << "Case #" << zz << ": NO\n";
			continue;
		}

		start.value = '1';
		while (curr % n != 0 && curr < all) {
			Quat current;
			current.value = data[curr % n];
			current.symbol = 1;
			start = mult(start, current);
			curr++;
		}
		int new_repeats = m - (curr / n);
		Quat to_mult;
		to_mult.symbol = 1;
		to_mult.value = '1';
		for (int i = 0; i < n; i++) {
			Quat current;
			current.value = data[curr % n];
			current.symbol = 1;
			to_mult = mult(to_mult, current);
			curr++;
		}
		for (int i = 0; i < new_repeats % 4; i++) {
			start = mult(start, to_mult);
		}
		if (start.value == '1' && start.symbol == 1) {
			cout << "Case #" << zz << ": YES\n";
		}
		else {
			cout << "Case #" << zz << ": NO\n";
		}
	}
	return 0;
}