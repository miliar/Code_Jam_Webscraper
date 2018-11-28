#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<size_t> primes;

bool isPrime(const size_t n, size_t & divider) {
	for (size_t i = 0; i < primes.size(); ++i) {
		if ((n != primes[i]) && !(n % primes[i])) {
			divider = primes[i];
			return false;
		}
	}
	return true;
}

void setPrimes(size_t max) {
	size_t dummy;
	if (primes.empty()) {
		primes.reserve(max);
		for (size_t n = 3; n <= max; n+=2) {
			if (isPrime(n, dummy)) {
				primes.push_back(n);
			}
		}
		primes.push_back(2);
	}
}

struct Number {
	Number(string s, size_t base) {
		value = 0;
		size_t factor = 1;
		for (size_t i = 0; i < s.size(); ++i) {
			value += (s[s.size()-i-1]-'0')*factor;
			factor*=base;
		}
	}

	size_t value;
};

string toBinary(size_t n) {
	string result;
	while (n) {
		result = string((n%2)?"1":"0")+result;
		n/=2;
	}
	return result;
}

void process(size_t n, size_t j) {
	const size_t max = Number(string(n, '1'), 2).value;
	const size_t min = Number(string(n-1, '1'), 2).value+2;
	setPrimes(max);
	string s;
	size_t divider;
	for (n = min; n <= max; n +=2) {
		if (!isPrime(n, divider)) {
			s = toBinary(n);
			ostringstream stream;
			stream << s << ' ' << divider;
			bool prime = false;
			for (size_t base = 3; !prime && (base <= 10); ++base) {
				size_t m = Number(s, base).value;
				prime |= isPrime(m, divider);
				if (!prime) {
					stream << ' ' << divider;
				}
			}
			if (!prime) {
				cout << stream.str() << endl;
				--j;
				if (!j) return;
			}
		}
	}
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		size_t n, j;
		cin >> n >> j;
		cout << "Case #" << inputNumber << ":" << endl;
		process(n,j);
	}
	return 0;
}
