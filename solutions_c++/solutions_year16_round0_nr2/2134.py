#include <iostream>

int main() { int cases; std::cin >> cases; std::cin.get(); // skip endline
	for (int n = 1; n <= cases; ++n) { std::cout << "Case #" << n << ": ";
		bool firstFlip = false;
		int inversions = 0;
		char prev = ' ';

		// std::cout << std::endl;
		for (char c = ' '; std::cin.get(c) && c != '\n'; ) {
			// std::cout << c << " " << firstFlip << " " << inversions << " " << prev << std::endl;
			if (prev == c)
				continue;
			if (c == '+' && prev == ' ')
				firstFlip = true;
			if (c == '-')
				inversions += 1;
			prev = c;
		}

		if (inversions > 0)
			std::cout << (firstFlip ? 1 : 0) + (2 * inversions - 1) << std::endl;
		else
			std::cout << 0 << std::endl;
	}
}
