#include <iostream>
#include <algorithm>
#include <vector>
#include <gmpxx.h>

#define MAX_N "100000000000000"

using namespace std;

vector<mpz_class> squares;

inline bool isPalindrome(mpz_class x) {
	string xStr = x.get_str();
	
	return xStr == string(xStr.rbegin(), xStr.rend());
}

int main(void) {
	mpz_class next = 1, square = 1, max(MAX_N);
	
	square = next * next;
	while (square <= max) {
		if (isPalindrome(square) && isPalindrome(next)) {
			squares.push_back(square);
		}
	
		next++;
		square = next * next;
	}
	
	int numCases;
	string a, b;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		cin >> a >> b;
		
		mpz_class first(a), last(b);
		
		cout << "Case #" << numCase << ": " << upper_bound(squares.begin(), squares.end(), last) - lower_bound(squares.begin(), squares.end(), first) << endl;
	}
}
