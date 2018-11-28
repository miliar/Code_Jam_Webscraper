#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <bitset>

using namespace std;

// const int N = 16;
const int N = 32;
const int N_HALF = N / 2;

int main() {
	int t, n, j;

	cin >> t >> n >> j;

	if (n != N) {
		cout << "ERROR!!!!" << endl;
		return 0;
	}

	cout << "Case #1:" << endl;
	for (int i = 0; i < j; i++) {
		bitset<N_HALF> bits(i);
		bits <<= 1;
		bits.set(0);
		bits.set(bits.size() - 1);
		cout << bits.to_string() << bits.to_string();

		bitset<N_HALF + 1> divisor;
		divisor.set(0);
		divisor.set(divisor.size() - 1);
		for (int base = 2; base <= 10; base++) {
			cout << " " << stoull(divisor.to_string(), nullptr, base);
		}
		cout << endl;
	}

	return 0;
}
