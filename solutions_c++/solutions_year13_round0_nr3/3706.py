#include <iostream>
#include <cstdio>
#include <cmath>

bool isSQRT(const double& num, long& square) {
	double possible = sqrt(num);
	square = possible;
	return possible == floor(possible);
}

bool isPalindrome(const long& num) {
	char buffer[20];
	int size(sprintf(buffer, "%ld", num));
	int medium(size >> 1);

	for (int i(0); i < medium; i++)
		if (buffer[i] != buffer[size - i - 1])
			return false;

	return true;
}

int main() {
	short num_test;
	std::cin >> num_test;

	for (short test(0); test < num_test; test++) {
		long A;
		long B;
		long count(0);
		long square;
		std::cin >> A >> B;

		for (long i(A); i <= B; i++) {
			// std::cout << "Num: " << i << "Pal: " << isPalindrome(i) << " Sqrt: " << isSQRT(i) << std::endl;
			if (isPalindrome(i) && isSQRT(i, square) && isPalindrome(square)) {
				// std::cout << "Valid: " << i << std::endl;
				count++;
			}
		}

		std::cout << "Case #" << (test + 1) << ": " << count << std::endl;
	}
}
