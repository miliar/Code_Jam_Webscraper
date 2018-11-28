#include <string>
#include <iostream>
#include <cmath>

#include "BigIntegerLibrary.hh"

#define N_PRIME 2000000

int primes[N_PRIME] = {0};
int idx_prime = 0;

void debug(std::string str) {
    std::cerr << "[debug] " << str << std::endl;
}

void output(std::string str) {
    std::cout << str << std::endl;
}

void calcPrimes() {
    primes[idx_prime] = 2;
    idx_prime++;
    int tester = 3;
    bool is_prime;
    while (idx_prime < N_PRIME) {
        is_prime = true;
        int sqrt_tester = (int)sqrt(tester);
        for(int i = 0; i < idx_prime && primes[i] <= sqrt_tester; i++) {
            if (tester % primes[i] == 0) {
                // out
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            primes[idx_prime] = tester;
            idx_prime++;
            if (idx_prime % 10000 == 0) {
                debug(std::string("Generated: ") + std::to_string(idx_prime) + " / " + std::to_string(N_PRIME));
            }
        }
        tester += 2;
    }
}

int searchPrimeFactor(BigUnsigned n) {
    int i = 0;
    BigUnsigned prime_bigint = primes[i];
    while (i < N_PRIME && prime_bigint < n) {
        if (n % prime_bigint == 0) {
            return primes[i];
        }
        i++;
        prime_bigint = primes[i];
    }
    return -1;
}

bool searchPrimeFactorsForArray(BigUnsigned (&num)[9], int (&prime_factors)[9]) {
    for (int i = 0; i < 9; i++) {
        int prime = searchPrimeFactor(num[i]);
        if (prime == -1) {
            return false;
        }
        prime_factors[i] = prime;
    }
    return true;
}

void convertToNumsOnBases(std::string& str_base2, BigUnsigned (&nums)[9]) {
    for (int i = 0; i < 9; i++) {
        int base = i + 2;
        BigUnsignedInABase num_base2_in_base(str_base2, base);
        nums[i] = num_base2_in_base;
    }
}

void solveAndOutputQ3(int n, int j) {
    debug("Calc primes");
    calcPrimes();
    debug("Done calc primes");
    // std::cout << primes[0] << " " << primes[1] << " " << primes[N_PRIME - 1];

    std::string lower_bound_str("1");
    for (int i = 0; i < n - 2; i++) {
        lower_bound_str += "0";
    }
    lower_bound_str += "1";

    BigUnsignedInABase num_base2_in_base(lower_bound_str, 2);
    BigUnsigned num_base2 = num_base2_in_base;
    int succeed_count = 0;
    while (true) {
        std::string str_base2 = num_base2_in_base;
        BigUnsigned nums_on_bases[9] = {0};
        convertToNumsOnBases(str_base2, nums_on_bases);
        debug(str_base2 + " "
            + bigUnsignedToString(nums_on_bases[0]) + " "
            + bigUnsignedToString(nums_on_bases[1]) + " "
            + bigUnsignedToString(nums_on_bases[2]) + " "
            + bigUnsignedToString(nums_on_bases[3]) + " "
            + bigUnsignedToString(nums_on_bases[4]) + " "
            + bigUnsignedToString(nums_on_bases[5]) + " "
            + bigUnsignedToString(nums_on_bases[6]) + " "
            + bigUnsignedToString(nums_on_bases[7]) + " "
            + bigUnsignedToString(nums_on_bases[8]) + " "
        );
        int prime_factors[9] = {0};
        bool found = searchPrimeFactorsForArray(nums_on_bases, prime_factors);
        if (found) {
            debug(std::string("bingo: ") + std::to_string(succeed_count + 1));
            output(str_base2 + " "
                + std::to_string(prime_factors[0]) + " "
                + std::to_string(prime_factors[1]) + " "
                + std::to_string(prime_factors[2]) + " "
                + std::to_string(prime_factors[3]) + " "
                + std::to_string(prime_factors[4]) + " "
                + std::to_string(prime_factors[5]) + " "
                + std::to_string(prime_factors[6]) + " "
                + std::to_string(prime_factors[7]) + " "
                + std::to_string(prime_factors[8])
            );
            succeed_count++;
            if (succeed_count >= j) {
                break;
            }
        } else {
            debug("failed");
        }
        num_base2 += 2;
        num_base2_in_base = BigUnsignedInABase(num_base2, 2);
    }

}

int main() {
    std::string case_line;
    std::cin >> case_line;
    int num_of_cases = std::stoi(case_line);

    // only one case
    std::string n_str;
    std::string j_str;
    std::cin >> n_str >> j_str;
    int n = std::stoi(n_str);
    int j = std::stoi(j_str);

    debug("debug");
    output("Case #1:");
    solveAndOutputQ3(n, j);

    return 0;
}
