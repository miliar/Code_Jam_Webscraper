#include <iostream>

#include <gmpxx.h>


void palindromize(std::string &s, int n)
{
	s.resize(n);
	for (int i = (n+1) / 2 ; i < n ; i ++) {
		s[i] = s[n - 1 - i];
	}
}

bool is_palindrom(std::string const &s)
{
	int n = s.size();

	for (int i = (n+1) / 2 ; i < n ; i ++) {
		if (s[i] != s[n - 1 - i])
			return false;
	}

	return true;
}

int main()
{
	int T;

	// Read the number of cases
	std::cin >> T;
	std::cin.exceptions(std::ios::goodbit);

	// For each case
	for (int t = 0 ; t < T ; t++) {
		mpz_class A, B;

		// Read the case
		std::cin >> A >> B;

		// Extract root palindrom left part
		mpz_class R(sqrt(A));
		std::string r = R.get_str(10);
		unsigned int nR = r.length(), nX = (nR+1) / 2;
		r.resize(nX); // Keep left part
		mpz_class X(r, 10);

		// Iterate from A to B
		mpz_class S;
		int count = 0;
		do
		{
			// Convert to base 10
			std::string x = X.get_str(10);

			// Check if the number of digits increased
			if (x.length() != nX) { // One more digit
				nR++;
				nX = (nR+1) / 2;
				x.resize(nX);
				X = mpz_class(x, 10);
			}

			// Build a palindrom from base
			palindromize(x, nR);

			// Compute square
			mpz_class Y(x, 10);
			S = Y*Y;

			if (S >= A && S <= B) {
				// Check if this square is a palindrome
				if (is_palindrom(S.get_str(10))) {
					count++;
				}
			}

			// Next base
			++X;
		}
		while(S <= B);

		std::cout << "Case #" << (t+1) << ": " << count << std::endl;
	}

	return 0;
}
