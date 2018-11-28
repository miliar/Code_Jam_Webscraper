#include <iostream>
using namespace std;

typedef unsigned long long ull;

const int MAX_N = 16;

ull pow[11][MAX_N + 1];

void computePowers() {
	for (int b = 2; b <= 10; b++) {
		pow[b][0] = 1;
		for (int i = 1; i <= MAX_N; i++)
			pow[b][i] = pow[b][i - 1] * b;
	}
}

ull valueFor(ull digits, int b) {
	if (b == 2)
		return digits;
	ull value = 0;
	for (int i = 0; i <= MAX_N; i++) {
		if (pow[2][i] & digits)
			value += pow[b][i];
	}
	return value;
}

ull anyDivisorOf(ull value) {
	if (value != 2 && value % 2 == 0)
		return 2;
	for (ull divisor = 3; divisor * divisor <= value; divisor += 2) {
		if (value % divisor == 0)
			return divisor;
	}
	return 1;
}

void print(ull binary, int n) {
	for (int i = n - 1; i >= 0; i--)
		if (pow[2][i] & binary)
			cout << '1';
		else
			cout << '0';
}

int main() {
	computePowers();
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << caseCounter << ":" << endl;
		for (ull i = 0; i < pow[2][n - 2]; i++) {
			ull candidate = pow[2][n - 1] ^ (i << 1) ^ 1;
			ull divisor[11];
			bool valid = true;
			for (int b = 2; b <= 10; b++) {
				ull valueOnBase = valueFor(candidate, b);
				divisor[b] = anyDivisorOf(valueOnBase);
				if (divisor[b] == 1) {
					valid = false;
					break;
				}
			}
			if (valid) {
				print(candidate, n);
				for (int b = 2; b <= 10; b++)
					cout << " " << divisor[b];
				cout << endl;
				j--;
				if (j == 0)
					break;
			}
		}
	}
	return 0;
}
