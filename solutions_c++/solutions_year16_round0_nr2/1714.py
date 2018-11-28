#include <iostream>
#include <string>

int main() {
	bool start;
	char prev;
	char next;
	unsigned int counter;
	unsigned int cases;
	std::string input;
	std::cin >> cases;
	for (unsigned int i = 1; i <= cases; i++) {
		std::cin >> input;
		counter = 0;
		if (input[0] == '+') start = true;
		else start = false;
		prev = input[0];
		for (auto it = ++(input.begin()); it < input.end(); it++) {
			next = *it;
			if (next != prev) counter++;
			prev = next;
		}
		if (!start && counter % 2 == 0) counter++;
		if (start && counter % 2 != 0) counter++;
		std::cout << "Case #" << i << ": " << counter << std::endl;
	}



	return 0;
}