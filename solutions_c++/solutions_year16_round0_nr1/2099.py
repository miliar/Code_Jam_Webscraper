#include <iostream>
#include <climits>

int main() {
	int t;
	std::cin >> t;
	
	unsigned long n, current, working, last;
	int digit, to_find;
	bool not_finished, digits[10]; // not found digits
	
	for (int i = 0; i < t; ++i) {
	
		to_find = 10;
		for (int d = 0; d < 10; ++d) {
			digits[d] = true;
		}
		
		std::cin >> n;
		not_finished = true;
		current = n;
		
		std::cout << "Case #" << i + 1 << ": ";
		if (n > 0) {
			while (
				to_find
			) {
				last = working = current;
				current += n;
				while (working > 0) {
					digit = working%10;
					working /= 10;
					if (digits[digit]) {
						digits[digit] = false;
						to_find--;
					}
				}
			}
		}
		if (to_find) {
			std::cout << "INSOMNIA";
		} else {
			std::cout << last;
		}
		
		std::cout << std::endl;
	}

	return 0;
}
