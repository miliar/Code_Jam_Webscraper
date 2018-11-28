#include <gmpxx.h>
#include <iostream>

bool palindrome(const mpz_class& number) {

        const std::string normal(number.get_str());
        const std::string reverse(normal.rbegin(), normal.rend());

        return normal == reverse;

}

int main() {

        int size;
        std::cin >> size;

#ifndef NDEBUG
        std::cerr << size << " intervals" << std::endl;
#endif

        for (int i = 1; i <= size; ++i) {

#ifndef NDEBUG
                std::cerr << std::endl << "Interval " << i << std::endl;
#endif

                mpz_class left, right;
                std::cin >> left >> right;

#ifndef NDEBUG
                std::cerr << "Left bound: " << left << std::endl << "Right bound: " << right << std::endl;
#endif

                mpz_class rleft(sqrt(left)), rright(sqrt(right));
                if (rleft * rleft < left) {
#ifndef NDEBUG
                        std::cerr << "Corrected incorrect left bound root (was " << rleft << ")" << std::endl;
#endif
                        ++rleft;
                }

#ifndef NDEBUG
                std::cerr << "Left bound root: " << rleft << std::endl << "Right bound root: " << rright << std::endl;
#endif

                mpz_class amount(0);

                for (mpz_class root(rleft); root <= rright; ++root) {

                        if (palindrome(root) and palindrome(root * root)) {
                                ++amount;
#ifndef NDEBUG
                                std::cerr << root << "^2 gives " << root * root << " and both are palindromes" << std::endl;
#endif
                        }

                }

                std::cout << "Case #" << i << ": " << amount << std::endl;

        }

}
