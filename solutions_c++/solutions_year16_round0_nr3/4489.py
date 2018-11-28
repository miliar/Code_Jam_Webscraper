#include <bitset>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <vector>

using u64 = uint64_t;

template<typename T>
T pow(const T& base, u64 exponent) {
    T retVal = 1;
    while (exponent--) {
        retVal *= base;
    }
    return retVal;
}

bool isPrime(u64 n, u64& divisor) {
    if (n <= 1) {
        // '1' is not prime
        divisor = 1;
        return false;
    } else if (n < 4) {
        // '2' and '3' are prime
        return true;
    } else if (n % 2 == 0) {
        // Multiples of '2' are not prime
        divisor = 2;
        return false;
    } else if (n < 9) {
        // '5' and '7' are prime
        return true;
    } else if (n % 3 == 0) {
        // Multiples of '3' are not prime
        divisor = 3;
        return false;
    }

    int limit = floor(sqrt(n));
    for (int i = 5; i <= limit; i += 6) {
        if (n % i == 0)
        {
            // Multiples are not primes
            divisor = i;
            return false;
        }
        else if (n % (i + 2) == 0) {
            // Multiples are not primes
            divisor = i + 2;
            return false;
        }
    }

    // Must be a prime
    return true;
}

bool validate(u64 length, u64 middle, std::vector<u64>& base_factors) {
    std::bitset<64> x((pow(2, length - 1) + 1) | (middle << 1));
    for (u64 i = 0; i < base_factors.size(); ++i) {
        u64 val = 0;
        for (u64 j = 0; j < 64; ++j) {
            val += x[j] ? pow(i + 2, j) : 0;
        }
        u64 divisor = 0;
        if (isPrime(val, divisor)) {
            return false;
        }
        base_factors[i] = divisor;
    }
    return true;
}

void solve(u64 length, u64 count) {
    u64 middle = 0ul;
    for (u64 n = 0ul; n < count; ++n) {
        for (; middle < pow(2, length - 2); ++middle) {
            std::vector<u64> base_factors(9, 0);
            if (validate(length, middle, base_factors)) {
                std::bitset<64> x(middle);
                std::stringstream ss;
                ss << x;
                std::string s;
                ss >> s;
                std::cout << "1" << s.substr(s.length() - length + 2) << "1";

                for (auto i : base_factors) {
                    std::cout << " " << i;
                }
                std::cout << std::endl;
                ++middle;
                break;
            }
        }
    }
}

int main() {
    u64 total = 0ul;
    std::cin >> total;

    for (u64 number = 1; number <= total; ++number) {
        u64 length = 0ul;
        u64 count = 0ul;
        std::cin >> length >> count;

        std::cout << "Case #" << number << ":" << std::endl;
        solve(length, count);
    }
}
