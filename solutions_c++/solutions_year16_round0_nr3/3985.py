#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <bitset>
#include <algorithm>

using namespace std;

unsigned long find_factor(unsigned long n) {
	for(unsigned long i = 2; i < 1000; i++) {
		if(n % i == 0) return i;
	}
	return 0;
}

unsigned long calc_base(unsigned long number, int base, int n){
	unsigned long result = 0;
	for(int i = 0; i < n; i++) {
		result += (number % 2) * pow(base, i);
		number /= 2;
	}
	return result;
}

template <typename T>
T powm(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

unsigned long test_mr(unsigned long a,unsigned long s,unsigned long d, unsigned long n) {
	unsigned long long a_pow = powm(a, d, n);
	if(a_pow == 1) return true;
	for(int i = 0; i < s + 1; i++) {
		if(a_pow == n - 1) return true;
		a_pow = (a_pow * a_pow) % n;
	}
	return a_pow == n - 1;
}

bool is_prime(unsigned long number) {
	if(number < 2) return false;
	if(number == 2 || number == 7 || number == 61) return true;

	unsigned long test[] = {2, 7, 61};
	unsigned long d = number - 1;
	unsigned long s = 0;
	while(d % 2 == 0) {
		d >>= 1;
		s++;
	}
	for(int i = 0; i < 3; i++) {
		if(!test_mr(test[i], s, d, number)) return false;
	}
	return true;
}

unsigned long solve(int n, int j){
	int found = 0;
	unsigned long prnt[9];
	unsigned long value = pow(2, n - 1) + 1;
	while(found < j) {
		for(int base = 2; base < 11; base++) {
			if(is_prime(calc_base(value, base, n))) break;
			if(base == 10) {
				bool cor = true;
				for(int i = 2; i <= 10; i++) {
					unsigned long fac = find_factor(calc_base(value, i, n));
					if(fac == 0) {
						cor = false;
						break;
					}
					prnt[i - 2] = fac;
				}
				if(cor) {
					cout << bitset<16>(value);
					for(int i = 2; i <= 10; i++) {
						cout << " " << prnt[i - 2];
					}
					cout << endl;
					found++;
				}
			}
		}
		value += 2;
	}

}

int main() {
	int t;
	int n, j;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		cin >> j;
		cout << "Case #1:" << endl;
		solve(n, j);
	}
	/*for(int i = 0; i < 100; i++) {
		if(is_prime(i))
			cout << i << endl;
	}*/

	return EXIT_SUCCESS;
}
