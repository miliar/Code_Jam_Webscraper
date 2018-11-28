// Fair & Square

#include <cassert>
#include <iostream>
#include <cmath>
#include <sstream>

bool isPalindrome(const long n) {
	assert(n >= 0);   // for non-negative integers only.
  long rev = 0;
	long num = n;
  while (num != 0) {
    rev = rev * 10 + num % 10;
    num /= 10;
  }
  return rev == n;
}

int nfairsquare(const long a, const long b) {
	int count = 0;
	long start = floor(sqrt(a));
	long end = floor(sqrt(b));

	for (long num = start; num <= end; num++) {
		if (isPalindrome(num)) {
			long square = num*num;
			if (b < square) break;

			if (a <= square && isPalindrome(square)) {
				count++;
			}
		}
	}

	return count;
}

int main(void) {
	std::string line;
	std::getline(std::cin, line);

	int ncases = std::stoi(line);
	for (int i = 0; i < ncases; i++) {
		long a, b;

		std::stringstream ss;
		std::getline(std::cin, line);
		ss << line;
		ss >> a >> b;

		int ans = nfairsquare(a, b);
		std::cout << "Case #" << (i+1) << ": " << ans << std::endl;
	}
	return 0;
}

