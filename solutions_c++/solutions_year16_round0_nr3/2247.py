#include <cmath>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;

int64_t firstDivisor(int64_t n) {
	int64_t root = sqrt(n);
	for (int64_t i = 2; i <= root; ++i) {
		if (!(n % i)) {
			return i;
		}
	}
	return 0;
}

int mod(int base, int exp, int divisor) {
	int result = 1;
	for (int i=0; i < exp; ++i) {
		result = (base * result) % divisor;
	}
	return result;
}

int firstDivisor(const vector<bool> &bin, int base) {
	for (int i = 2; i < 100; ++i) {
		int val = 0;
		for (int j = 0; j < bin.size(); ++j) {
			if (bin[j]) {
				val = (val + mod(base, bin.size() - 1 - j, i)) % i;
			}
		}
		if (val == 0) {
			return i;
		}
	}
	return 0;
}

bool checkBin(ofstream &out, const vector<bool> &bin) {
	stringstream ss;
	for (int i=0; i < bin.size(); ++i) {
		ss << bin[i] ? '1' : '0';
	}
	for (int i=2; i <= 10; ++i) {
		int divisor = firstDivisor(bin, i);
		if (divisor == 0) {
			return false;
		}
		ss << ' ' << divisor;
	}
	out << ss.str() << endl;
	return true;
}

void increment(vector<bool> &bin) {
	for (int i = bin.size() - 2; i >= 0; --i) {
		if (!bin[i]) {
			bin[i] = true;
			return;
		} else {
			bin[i] = false;
		}
	}
}

int main() {
	ifstream infile("C-large.in");
	ofstream outfile("C.out");
	
	int T, N, J;
	infile >> T;
	for (int i=0; i < T; ++i) {
		infile >> N >> J;
		outfile << "Case #" << i+1 << ':' << endl;
		vector<bool> bin;
		int numFound = 0;
		bin.resize(N);
		bin[0] = bin[N - 1] = true;
		while (numFound < J && bin[0]) {
			numFound += checkBin(outfile, bin);
			increment(bin);
		}
		if (!bin[0]) {
			cout << "Failed to find all jamcoins" << endl;
		}
	}
}
