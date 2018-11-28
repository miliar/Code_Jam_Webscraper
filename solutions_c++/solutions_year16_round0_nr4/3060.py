#include <iostream>
#include <bitset>

int main (int argc, char * argv[]) {
    size_t number_of_test_cases;
    std::cin >> number_of_test_cases;
    for (size_t test_case_number = 1; test_case_number <= number_of_test_cases; ++test_case_number) {
        size_t K, C, S, result;
        std::cin >> K >> C >> S;

        std::cout << "Case #" << test_case_number << ":";
        for (size_t i = 1; i <= K; ++i) 
            std::cout << " " << i;
        std::cout << std::endl;
    }
}