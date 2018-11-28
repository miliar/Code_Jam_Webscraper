#include <iostream>

int main() {
	int tests;
	std::cout.precision(10);
	std::cin >> tests;
	for (int i = 1; i <= tests; ++i) {
		double C, F, X;
		std::cin >> C >> F >> X;

		int n = 0; // number of farms to make
		double seconds = 0;
		while ( (C/(2+n*F)) + (X/(2+(n+1)*F)) < (X/(2+n*F)) ) {
			seconds += (C/(2+n*F));
			++n;
		}
		seconds += (X/(2+n*F));
		std::cout << "Case #" << i << ": " << seconds << std::endl;
	}
	return 0;
}
