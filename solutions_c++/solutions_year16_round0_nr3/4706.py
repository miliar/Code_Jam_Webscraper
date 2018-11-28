#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int64_t power[9][32];

void init() {
	for (int64_t i = 2; i <= 10; i++) {
		power[i - 2][0] = 1;
		for (int64_t ii = 1; ii < 32; ii++)
			power[i - 2][ii] = power[i - 2][ii - 1] * i;
	}
}

int64_t getVal(int64_t *num, int64_t base, int64_t len) {
	int64_t val = 0;
	for (int64_t i = 0; i < len; i++) {
		val += num[i] * power[base - 2][i];
	}
	return val;
}

int64_t getDivisor(int64_t num) {
	int64_t s = sqrt(num);
	for (int64_t i = 2; i <= s; i++) {
		if (num % i == 0)
			return i;
	}
	return 1;
}

int tarr[9];

int64_t check(int64_t *num, int64_t len) {
	int64_t base;
	int64_t ai = 0;
	for (base = 2; base <= 10; base++) {
		int64_t divisor = getDivisor(getVal(num, base, len));
		if (divisor == 1)
			return 0;
		tarr[ai++] = divisor;
	}
	return 1;
}

void next(int64_t *num, int64_t len, int64_t c) {
	for (int64_t i = 1; i < len - 1; i++) {
		num[i] = c & (1 << (i - 1)) ? 1 : 0;
	}
}

int main() {
	ifstream input;
	input.open("in.txt", ios::in);

	int64_t testCases = 0;
	input >> testCases;

	init();

	for (int64_t c = 1; c <= testCases; c++) {
		int64_t n, j;
		input >> n >> j;
		int64_t num[32] = { 0 };
		num[0] = num[n - 1] = 1;
		int64_t found = 0;
		int64_t counter = 0;
		cout << "Case #1:" << endl;
		while (1) {
//			if (counter % 1 == 0) {
//				cout << "Testing : " << counter << " ";
//				for (int64_t o = 0; o < n; o++)
//					cout << num[o];
//				cout << endl;
//			}
			if (check(num, n) == 1) {
				found++;
				for (int64_t o = n - 1; o >= 0; o--)
					cout << num[o];
				for (int o = 0; o < 9; o++)
					cout << " " << tarr[o];
				cout << endl;
				if (found == j)
					break;
			}
			next(num, n, ++counter);
		}
	}
	return 0;
}
