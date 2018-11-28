#include <vector>
#include <cstdint>
#include <iostream>
#include <fstream>
using namespace std;

void add_numer(vector<bool> &mask, int64_t n) {
	if (n == 0) {
		mask[0] = true;
		return;
	}
	while (n > 0) {
		mask[n % 10] = true;
		n /= 10;
	}
}

bool check_mask(vector<bool> &mask) {
	for (bool x : mask) {
		if (!x)
			return false;
	}
	return true;
}

int64_t test(int64_t x) {
	vector<bool> mask(10, false);
	int64_t n = 0;
	if (x == 0)
		return -1;
	while (!check_mask(mask)) {
		if (n > 10000) {
			cout << "Bad number: " << x << endl;
			return -1;
		}
		add_numer(mask, ++n * x);
	}
	return n * x;
}

int main() {
	int t = 0;
	int64_t x;

	ifstream in("D:\\Sources\\C++\\CodeJam\\2016\\stage_1\\in.txt");
	ofstream out("D:\\Sources\\C++\\CodeJam\\2016\\stage_1\\out.txt");
	in >> t;
	for (int i = 1; i <= t; i++) {
		in >> x;
		x = test(x);
		if (x == -1)
			out << "Case #" << i << ": INSOMNIA" << endl;
		else
			out << "Case #" << i << ": " << x << endl;
	}
	return 0;
}

