#include <iostream>
#include <string>

bool extractDigits(uint64_t value, uint16_t &set) {
	if (!value)
		return false;
	while (value) {
		uint64_t digit = value % 10;
		value /= 10;
		set |= 1 << digit;
	}
	return true;
}

std::string do_work(uint64_t n) {
	uint16_t set = 0;
	int i = 1;
	bool ret;
	while ((ret = extractDigits(n * (i++), set)) && set != 0x3FF);
	if (!ret)
		return "INSOMNIA";
	return std::to_string(n * (i-1));
}

int main() {
	int t, n;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cin >> n;
		std::cout << "Case #" << i << ": " << do_work(n) << std::endl;
	}
	return 0;
}
