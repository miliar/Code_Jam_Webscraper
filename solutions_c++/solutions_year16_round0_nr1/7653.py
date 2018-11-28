#include <iostream>
#include <set>

std::string count_sheep(const unsigned int N)
{
	unsigned int n = N;
	std::set<char> chars;

	while (true) {
		std::string number = std::to_string(n);

		for (auto it = number.cbegin(); it != number.cend(); ++it) {
			chars.insert(*it);

			if (chars.size() == 10)
				return number;
		}

		n += N;
	}

	return "";
}

int main()
{
	unsigned int T, N;
	std::string output;

	std::cin >> T;

	for (unsigned int i = 0; i < T; i++) {
		std::cin >> N;

		if (N == 0)
			output = "INSOMNIA";
		else
			output = count_sheep(N);

		std::cout << "Case #" << i + 1 << ": " << output << '\n';
	}

	return 0;
}
