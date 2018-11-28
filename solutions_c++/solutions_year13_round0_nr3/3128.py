
#include <iostream>
#include <sstream>
#include <string>

#include <gmp.h>
#include <gmpxx.h>

bool isPalindrone(mpz_class x);

int main(void)
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; t++) {
	std::cout << "Case #" << t << ": ";
	int count = 0;
	mpz_class lo, hi;
	std::cin >> lo >> hi;
	
	mpz_class curr, end;
	curr = sqrt(lo);
	end = sqrt(hi);
	while (curr <= end) {
	    if (isPalindrone(curr)) {
		mpz_class sqr = curr * curr;
		if (sqr < lo) { // ignore 
		} else if (isPalindrone(sqr)) {
		    //std::cout << " " << sqr << " ";
		    count++;
		}
	    }
	    curr++;
	}

	std::cout << count << std::endl;
    }
}

bool isPalindrone(mpz_class x) {
    std::stringstream ss;
    std::string asString;
    ss << x;
    ss >> asString;
    int len = asString.size();
    for (int i = 0; i < len/2; i++) {
	if (asString[i] != asString[len - (i + 1)]) {
	    return false;
	}
    }
    return true;
}
