#include <iostream>
#include <bitset>
#include <vector>
#include <cassert>

typedef std::bitset<32> number_t;

const size_t bigger_prime = 200000000;
std::bitset<bigger_prime> is_prime;

void calc_primes()
{
    std::cerr << "Calculating primes..." << std::flush;
    is_prime.set();
    is_prime.reset(0);
    is_prime.reset(1);
    for (size_t i = 2; i < bigger_prime; ++i) {
        if (is_prime.test(i)) {
            for (size_t j = 2 * i; j < bigger_prime; j += i) {
                is_prime.reset(j);
            }
        }
    }
    std::cerr << "done." << std::endl;
}

std::ostream & operator<< (std::ostream & os, const number_t & number)
{
    std::string s = number.to_string();
    size_t i = s.find('1');
    s.erase(0, i);
    os << s;
    return os;
}

void increment (number_t & number)
{
    for (size_t pos = 1;; ++pos) {
        assert(pos != 31);
        number.flip(pos);
        if (number[pos])
            break;
    }
}

size_t get_divider(const number_t & number, const size_t base)
{
    size_t num = 0, mul = 1;
    for (size_t i = 0; i < 32; ++i) {
        num += number[i] * mul;
        mul *= base;
    }
    
    
    for (size_t i = 2; i*i < num; ++i) {
        assert(i < bigger_prime);
        if (!is_prime.test(i)) continue;
        if (num % i == 0) return i;
    }
    return 0;
}

int main (int argc, char * argv[]) {
    calc_primes();
    size_t number_of_test_cases;
    std::cin >> number_of_test_cases;
    for (size_t test_case_number = 1; test_case_number <= number_of_test_cases; ++test_case_number) {
        size_t N, J;
        std::cin >> N >> J;
        std::cout << "Case #" << test_case_number << ":" << std::endl;
        number_t number;
        number.set(0);
        number.set(N-1);
        while (J) {
            std::vector<size_t> dividers;
            for (size_t base = 2; base <= 10; ++base) {
                size_t divider = get_divider(number, base);
                if (divider == 0)
                    break;
                dividers.push_back(divider);
            }
            if (dividers.size() != 9) {
                increment(number);
                continue;
            }

            --J;
            std::cout << number;
            for (auto div : dividers) std::cout << " " << div;
            std::cout << std::endl;
            increment(number);
        }
    }
}