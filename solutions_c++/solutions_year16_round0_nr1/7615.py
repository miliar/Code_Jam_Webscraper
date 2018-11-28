
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> read_input() {

	std::vector<std::string> input_buffer;
	while (!std::cin.eof()) {
		std::string s;
		std::cin >> s;
		if (!s.empty()) {
			input_buffer.push_back(std::move(s));
		}
	}

	return input_buffer;
}

unsigned long long check(unsigned long long n) {
	const int LOOP_MAX = 1000;
	int f = (1 << 10) - 1;
	unsigned long long max = 0;
	for (int i = 0; i < LOOP_MAX; ++i) {
		unsigned long long nn = (i + 1) * n;
		while (nn > 0) {
			int bf = f;
			f &= ~(1 << (nn % 10));
			nn /= 10;
			if (f != bf) {
				max = (i + 1) * n;
			}
		}
	}
	if (f > 0) {
		return 0;
	}
	return max;
}

int main(void) {
	std::ios::sync_with_stdio(false);

	std::string s;
	std::cin >> s;
	int T = std::stoi(s);
	const auto input_buffer = std::move(read_input());

	int c = 0;
	for (const auto& n : input_buffer) {
		++c;
		unsigned long long l = std::stoull(n);
		unsigned long long ans = check(l);
		std::cout << "Case #" << c << ": ";
		if (ans == 0) {
			std::cout << "INSOMNIA";
		}
		else {
			std::cout << ans;
		}
		std::cout << std::endl;
	}

	return 0;

}
