#include <iostream>
#include <string>
#include <math.h>

std::string tobinstr(int b, int w) {
	std::string ans = "";
	while (w --) {
		if (b & 1) ans = std::string("1") + ans;
		else ans = std::string("0") + ans;
		b >>= 1;
	}
	return ans;
}

long long toint(std::string s, long long b) {
	long long ans = 0, base = 1;
	for (int i = s.length() - 1; i >= 0; i --) {
		if (s[i] == '1') ans += base;
		base *= b;
	}
	return ans;
}

long long is_prime(long long n) {
	long long top = sqrt(n);
	if (n < 2) return false;
	if (n == 2) return true;
	for (long long i = 2; i < top; i ++)
		if (n % i == 0) return i;
	return -1;
}

void find(int n, int m) {
	for (int i = 0; i < (1 << (n - 2)); i ++) {
		std::string str = "1" + tobinstr(i, n - 2) + "1";
		int prime[20];
		bool found = true;
		for (int j = 2; j <= 10; j ++) {
			long long cur = toint(str, j);
			//std::cout << cur << std::endl;
			prime[j] = is_prime(cur);
			if (prime[j] == -1) {
				found = false;
				break;
			}
		}
		if (found) {
			std::cout << str;
			for (int j = 2; j <= 10; j ++)
				std::cout << " " << prime[j];
			std::cout << std::endl;
			m --;
			if (m == 0) return;
		}
	}
}	

int main() {
	std::cout << "Case #1:" << std::endl;
	find(16, 50);
	return 0;
}
