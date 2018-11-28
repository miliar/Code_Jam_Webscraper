#include <iostream>
#include <cstdio>
#include <streambuf>
#include <array>
#include <cstdio>

struct Digits {
public:
	int digits_left = 10;
	std::array<bool, 10> digits;
	Digits() {
		clear();
	}
	void clear() {
		digits_left = 10;
		digits.fill(false);
	}
protected:
	void set_digit(unsigned digit) {
		if (!digits[digit]) {
			digits[digit] = true;
			digits_left--;
		}
	}
public: 
	bool evaluate(unsigned v) {
		do {
			set_digit(v % 10);
			v = v / 10;
		}
		while (v != 0 && !is_over());
		
		return is_over();
	}
	bool is_over() {
		return digits_left == 0;
	}
};


void problemA() {
	Digits digits;
	unsigned v;
	unsigned num_tests;
	std::cin >> num_tests;

	for (int i = 1; i <= num_tests; i++) {
		std::cin >> v;

		if (v == 0) {
			std::cout <<"Case #" << i << ": INSOMNIA\n";
		}
		else {
			unsigned current_v = 0;
			while (!digits.is_over()) {
				current_v += v;
				digits.evaluate(current_v);
			}
			std::cout << "Case #" << i << ": " << current_v << "\n";
			digits.clear();
		}
	}
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	problemA();
}