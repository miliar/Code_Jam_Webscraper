#include <iostream>
#include <set>

long long cnt(unsigned long long n) {
	if (n == 0) return -1;
	std::set <int> digit;
	for (unsigned long long i = 1; digit.size() < 10; i ++) {
		unsigned long long m = n * i;
		while (m) {
			digit.insert(m % 10);
			m /= 10;
		}
		if (digit.size() == 10) return n * i;
	}
	return -1;
}

int main() {
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; i ++) {
		long long ipt;
		std::cin >> ipt;
		long long ans = cnt(ipt);
		std::cout << "Case #" << i << ": ";
		if (ans == -1)  std::cout << "INSOMNIA" << std::endl;
		else std::cout << ans << std::endl;
	}
	return 0;
}
