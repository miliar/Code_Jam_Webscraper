#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

bool isPrime(long long num) {
	for (long long i = 2; i * i < num; i++) {
		if (num % i == 0) return false;
	}
	return true;
}

void solve(int c) {
	std::cout << "Case #" << c << ":" << std::endl;
	long long n, j;
	std::cin >> n >> j;

	int count = 0;
	for (long long i = 1 << (n - 1); i < (1 << n) && count < j; i++) {
		if (i % 2 == 0) continue;
		std::string s = "";
		long long m = i;
		while (m != 0) {
			s += static_cast<char>('0' + m % 2);
			m /= 2;
		}

		std::reverse(s.begin(), s.end());
		std::vector<long long> d;
		for (int j = 2; j < 11; j++) {
			long long t = 0;
			for (int k = 0; k < s.length(); k++) {
				if (s[s.length() - 1 - k] == '1') {
					t += std::pow(j, k);
				}
			}
			if (isPrime(t)) break;
			d.push_back(t);
		}
		if (d.size() != 9) continue;

		std::vector<long long> v;
		std::cout << s << " ";
		for (long long t = 0; t < d.size(); t++) {
			for (long long k = 3; k < d[t]; k++) {
				if (d[t] % k == 0) {
					v.push_back(k);
					break;
				}
			}
		}

		for (int k = 0; k < v.size(); k++) {
			std::cout << v[k];
			if (k != v.size() - 1) std::cout << " ";
		}
		std::cout << std::endl;
		count++;
	}
}

int main() {
	int t;

	std::cin >> t;

	for (int i = 0; i < t; i++) {
		solve(i + 1);
	}
}