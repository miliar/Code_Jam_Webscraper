#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cout << "Case #1:\n";
	int count = 50;
	for(int n = 0x8001; count; n += 2) {
		vector<long long> divisors(9);
		bool valid = true;
		for(int base = 2; base <= 10; ++base) {
			long long number = 0;
			for(int i = 15; i >= 0; --i) {
				number = number * base + (n >> i & 1);
			}
			bool prime = true;
			for(long long d = 2; d * d <= number; ++d) {
				if(number % d == 0) {
					prime = false;
					divisors[base - 2] = d;
					break;
				}
			}
			if(prime) {
				valid = false;
				break;
			}
		}
		if(valid) {
			for(int i = 15; i >= 0; --i) {
				cout << (n >> i & 1);
			}
			for(long long d : divisors) {
				cout << ' ' << d;
			}
			cout << '\n';
			--count;
		}
	}
	return 0;
}
