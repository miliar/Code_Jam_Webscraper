#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <set>
#include <vector>
#include <string.h>

using namespace std;

int cmp(const void *x, const void *y) {
	// Implement when needed
	return 0;
}

int cmp(const int x, const int y) {
	return x - y;
}

int cmp(const double x, const double y) {
	return x - y;
}

int cmp(const char *x, const char *y) {
	int s1 = x ? strlen(x) : 0;
	int s2 = y ? strlen(y) : 0;
	if (s1 != s2) return s1 - s2;
	if (!s1) return 0;
	return strcmp(x, y);
}

int cmp(const string x, const string y) {
	return x.compare(y);
}

#define MAX(x, y) (cmp((x), (y)) > 0 ? (x) : (y))
#define MIN(x, y) (cmp((x), (y)) < 0 ? (x) : (y))

long long pow_table[9][16];

void fillPowTable() {
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 16; j++)
			pow_table[i][j] = (long long) pow((i + 2), j);
}

long long toBase(long long num, int bitcnt, int base) {
	long long output = 0;
	if (base == 2) return num;
	for (int i = 0; i < bitcnt; i++)
		if (num & (1 << i))
			output += pow_table[base - 2][i];
	return output;
}

long long divisor[9];
bool isJamCoin(long long num, int bitcnt) {
	for (int i = 2; i <= 10; i++) {
		long long tmp = toBase(num, bitcnt, i);
		long long max = (int) sqrt(tmp);
		bool found = false;

		for (int j = 2; j <= max; j++)
			if (tmp % j == 0){
			       	divisor[i - 2] = j;
				found = true;
				break;
			}
		if (!found) return false;
	}
	return true;
}

int main() {
	int t, n, j, cnt = 0;
	long long num, max;

	fillPowTable();

	cin >> t >> n >> j;
	num = 1 + (1 << (n - 1));
	max = (1 << n) - 1;

	cout << "Case #1:" << endl;
	while (cnt < j && num <= max) {
		if (isJamCoin(num, n)) {
			for (int i = n - 1; i >= 0; i--) cout << ((num & (1 << i)) ? 1 : 0);
			cout << " ";
			for (int i = 0; i < 9; i++) cout << divisor[i] << " ";
			cout << endl;
			cnt++;
		}
		num += 2;
	}

	return 0;
}

