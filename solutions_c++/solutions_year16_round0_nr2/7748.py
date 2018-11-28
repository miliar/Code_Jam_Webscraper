#include <iostream>

int main()
{
	std::string stack;
	unsigned int T;
	std::cin >> T;

	for (int i = 0; i < T; i++) {
		unsigned int flips = 0;
		std::string::size_type start = 0;

		std::cin >> stack;

		while (true) {
			// first '+' after start
			std::string::size_type pos = stack.find('+', start);

			if (pos == std::string::npos)
				pos = stack.size() + 1;

			// '-' from start to pos

			if (start > 0) ++flips;
			/* flip('-', 0, start - 1); */

			if (pos > 0) ++flips;
			/* flip('+', 0, pos - 1); // flip from 0 to pos - 1 to get only '+' */

			// '+' from 0 to pos

			if (pos + 1 >= stack.size())
				break;

			// first '-' after pos
			pos = stack.find('-', pos + 1);

			// stack full of '+' !
			if (pos == std::string::npos)
				break;

			// start at first '-'
			start = pos;
		}

		std::cout << "Case #" << i + 1 << ": " << flips << '\n';
	}

	return 0;
}
