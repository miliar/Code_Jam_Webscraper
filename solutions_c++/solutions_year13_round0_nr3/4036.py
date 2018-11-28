#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <unordered_map>
#include <functional>
#include <utility>
#include <memory>
#include <unordered_set>
#include <set>
#include <algorithm>
using namespace std;

bool isPalindrome(unsigned long long i) {
	unsigned long long out = i % 10;
	i /= 10;
	while(i > out) {
		out *= 10;
		out += i % 10;
		i /= 10;
	}
	return i == out || i == out / 10;
}

unsigned long long getPalindrome(bool odd, unsigned long long i) {
	unsigned long long out = odd ? i / 10 : i;
	while(i) {
		out *= 10;
		out += i % 10;
		i /= 10;
	}
	return out;
}

set<unsigned long long> cache;

#define BOUND 10000000ULL

void prepare() {
	for(int i = 1;; ++i) {
		unsigned long long p = getPalindrome(true, i);
		if(p > BOUND) return;
		unsigned long long sp = p * p;
		if(isPalindrome(sp)) cache.insert(sp);

		p = getPalindrome(false, i);
		if(p <= BOUND) {
			sp = p * p;
			if(isPalindrome(sp)) cache.insert(sp);
		}
	}
}

unsigned next() {
	unsigned long long A, B;
	cin >> A >> B;
	auto a = cache.lower_bound(A);
	auto b = cache.upper_bound(B);
	unsigned out = 0;
	while(a != b) {
		++a;
		++out;
	}
	return out;
}

int main() {
	prepare();
	int T;
	cin >> T;
	for(int t = 0; t < T; ++t) {
		cout << "Case #" << t + 1 << ": " << next() << endl;
	}
}
