#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

#include <emmintrin.h>
#include <gmpxx.h>

// 0 = prime, 1 = divisor maybe too big, 2 = divisor
mpz_class get_prime_result(mpz_class& nb) {
    mpz_class nb_sqrt = sqrt(nb);
    mpz_class two(2);

    if(nb % mpz_class(2) == 0)
        return mpz_class(2);
    for(mpz_class i = 3 ; i <= nb_sqrt ; i+=2) {
        // Too big, we skip
        if(i > 300000)
            return mpz_class(1);
        if(nb % i == 0)
            return i;
    }
    return 0;
}

bool is_prime(mpz_class& nb) {
    return (mpz_probab_prime_p(nb.get_mpz_t(), 15)) > 0;
}

std::string bintostr(std::uint32_t binary) {
    std::string output;
    do {
        if(binary & 1)
            output.push_back('1');
        else
            output.push_back('0');

        binary >>= 1;
    } while(binary != 0);
    std::reverse(output.begin(), output.end());
    return output;
}

bool test_jamcoin(std::uint32_t jamcoin) {
    std::string bin_string = bintostr(jamcoin);
    std::vector<std::string> divisors;

    // We first test for each base if the number is a primer one using GMP (Miller Rabin algorithm)
    for(int i = 2 ; i < 11 ; i++) {
        mpz_class integer(bin_string, i);
        if(is_prime(integer)) {
            return false;
        }
    }

    // If those aren't prime, we can search for their divisors
    for(int i = 2 ; i < 11 ; i++) {
        mpz_class integer(bin_string, i);
        mpz_class prime_result = get_prime_result(integer);
        if(prime_result == 0) {
            return false;
        // Couldn't find a divisor quickly: skipped
        } else if(prime_result == 1) {
            return false;
        } else {
            divisors.push_back(prime_result.get_str());
        }
    }

    std::cout << bin_string;
    for(std::vector<std::string>::size_type i = 0 ; i < divisors.size() ; i++) {
        std::cout << " " << divisors[i];
    }
    std::cout << std::endl;
    return true;
}

inline constexpr
std::uint32_t plus_one(std::uint32_t jamcoin) {
    return (((jamcoin >> 1) + 1) << 1) + 1;
}

int main() {
    unsigned int T, N, J;
    std::cin >> T >> N >> J;

    std::uint32_t init = (1 << (N - 1)) + 1;
    unsigned int jamcoins_found = 0;
    std::cout << "Case #1:" << std::endl;
    for(;;) {
        if(test_jamcoin(init)) {
            jamcoins_found++;
        }

        if(jamcoins_found == J)
            break;

        init = plus_one(init);
    }

    return EXIT_SUCCESS;
}
