#include <iostream>
#include <bitset>

void collect_digits(std::bitset<10> & digits, size_t number) {
    while (number != 0) {
        digits.set(number % 10);
        number /= 10;
    }
}

int main (int argc, char * argv[]) {
    size_t number_of_test_cases;
    std::cin >> number_of_test_cases;
    for (size_t test_case_number = 1; test_case_number <= number_of_test_cases; ++test_case_number) {
        size_t N;
        std::cin >> N;
        
        std::cout << "Case #" << test_case_number << ": ";
        if (N == 0) {
            std::cout << "INSOMNIA" << std::endl;
            continue;
        }
            
        std::bitset<10> digits;
        size_t number = 0;
        while (!digits.all()) {
            number += N;
            collect_digits(digits, number);
            if (number < N) std::cerr << "OVERFLOW!!!" << std::endl;
        }
        std::cout << number << std::endl; 
    }
}