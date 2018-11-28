#include "CountingSheep.h"

bool CountingSheep::isSleep() {
	for (int i = 0; i < 10; i++) {
		if (!digit[i]) {
			return false;
		}
	}
	return true;
}

long CountingSheep::counting() {
	for (long i = 2; number_modify != last_num; i++) {
		scanDigit();
		if (isSleep()) {
			return number_modify;
		}
		else {
			last_num = number_modify;
			number_modify = number * i;
		}
	}
	return -1;
}

void CountingSheep::scanDigit() {
	long temp = number_modify;
	while (temp) {
		digit[temp % 10] = true;
		temp /= 10;
	}
}

int main() {
	long t, n;
	std::cin >> t;
	for (unsigned long i = 1; i <= t; i++) {
		std::cin >> n;
		CountingSheep cs(n);
		n = cs.counting();
		if (n == -1) {
			std::cout << "Case #" << i << ": INSOMNIA" << std::endl;
		}
		else {
			std::cout << "Case #" << i << ": " << n << std::endl;
		}
	}
	return 0;
}