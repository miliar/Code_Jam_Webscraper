#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <string>
#include "bigint\BigIntegerLibrary.hh"  // source from : https://mattmccutchen.net/bigint/

using namespace std;

BigInteger powers(BigInteger base, int power) {
	BigInteger x(1);
	for (int i = 0; i < power; i++) {
		x *= base;
	}
	return x;
}

BigInteger prime(BigInteger n) {
	BigInteger i(2);
	for (; i  < 100000; ++i) {
		if (n % i == 0)
			return i;
	}
	return BigInteger(0);
}

BigInteger transfer(int base, BigInteger n) {
	if (base == 10)
		return n;
	BigInteger res;
	int power = 0;
	while (n > 0) {
		BigInteger t = n % 10;
		if (bigIntegerToString(t) == "1")
			res += powers(base, power);
		power++;
		n /= 10;
	}
	return res;
}

BigInteger nextN(BigInteger n) {
	BigInteger temp = n / 10;
	int count = 1;
	for (;; ++count) {
		if (temp % 10 == 0)
			break;
		temp /= 10;
	}
	BigInteger num = powers(10, count);
	n = (n + num) / num*num + 1;

	return n;
}

int main() {
	ifstream in("C-large.in");
	ofstream out("largeoutput.txt");
	int cases, num;
	in >> cases;
	for (num = 1; num <= cases; ++num) {
		int N, J;
		in >> N >> J;
		out << "Case #" << num << ":" << endl;
		BigInteger n = powers(BigInteger(10), N - 1) + 1;
		for (int i = 0; i < J; ) {
			bool primeFlag = true;
			vector<BigInteger> divisors;
			for (int base = 2; base <= 10; ++base) {
				BigInteger baseNum = transfer(base, n);
				BigInteger primeNum = prime(baseNum);
				if (primeNum == 0) {
					primeFlag = false;
					break;
				}
				divisors.push_back(primeNum);
			}

			if (primeFlag) {
				i++;
				out << n << " ";
				for (auto p : divisors) {
					out << p << " ";
				}
				out << endl;
			}
			cout << n << endl;
			n = nextN(n);
		}
	}
	return 0;
}