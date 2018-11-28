#include <algorithm>
#include <iostream>
#include <iterator>
#include <bitset>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

#define TYPE unsigned long long
#define f(i, N) for(unsigned i = 0; i < N; ++i)
#define fr(i, N) for(int i = N-1; i >= 0; --i) // reverse
#define ff(i, j, N) for(unsigned i = 0; i < N; ++i) for(unsigned j = 0; j < N; ++j)
#define V vector<TYPE>

const TYPE J = 50, N = 16;

bitset<N> bits;

bool incr() {
	for (int i = 1; i < bits.size()-1; ++i) {
		bits.flip(i);
		if (bits[i]) return true;
	}
	return false;
}

TYPE toBase(int base) {
	TYPE r = 0;
	TYPE current = 1;
	f(i, bits.size()) {
		if (bits[i]) r += current;
		current *= base;
	}

	return r;
}

TYPE isPrime(TYPE n) {
	TYPE till = sqrt(n);
	for (TYPE i = 3; i <= till; ++i) {
		if (n % i == 0) return i;
	}
	return 0;
}

void printbits(string s = "") {
	fr(i, bits.size()) {
		cout << (bits[i] ? "1" : "0");
	}
	cout << s;
}

void solve(TYPE N, TYPE J)
{
	bits[0] = true;
	bits[N-1] = true;
	do {
		vector<TYPE> divs;
		for (int i = 2; i <= 10; ++i) {
			auto n = toBase(i); // using bits
			auto p = isPrime(n);
			if (p == 0) break;
			divs.push_back(p);
		}
		if (divs.size() == 9) {
			--J;
			printbits(" ");
			std::copy(divs.begin(), divs.end(), std::ostream_iterator<TYPE>(std::cout, " "));
			cout << endl;
		}
	} while (incr() && J > 0);
}

int main() {
	unsigned T = 1;
	f(t, T) {
		try {
			cout << "Case #" << t + 1 << ": " << endl;
			solve(N, J);
		}
		catch (const std::exception& e) {
			cout << e.what() << endl;
		}
		catch (...) {
			cout << "Unknown exception" << endl;
		}
	}
}