#include <iostream>

int main()
{
	unsigned int cases;
	unsigned long long startNumber;
	unsigned long long number;
	unsigned long long helper;
	unsigned long long seenNumber;
	bool isDone = false;
	std::cin >> cases;
	for (unsigned int a = 1; a <= cases; a++) {
		std::cin >> startNumber;
		number = startNumber;
		if (number == 0) {
			std::cout << "Case #" << a << ": INSOMNIA\n";
			continue;
		}
		bool seen[10] = { false };
		unsigned int counter = 1;
		while (true) {
			isDone = true;
			helper = number;
			while (helper != 0) {
				seenNumber = helper % 10;
				seen[seenNumber] = true;
				helper /= 10;
			}
			for (int i = 0; i < 10; i++) {
				if (seen[i] == false) {
					isDone = false;
					break;
				}
			}
			if (isDone) {
				std::cout << "Case #" << a << ": " << number << std::endl;
				break;
			}
			counter++;
			number = counter * startNumber;
		}
	}


    return 0;
}

