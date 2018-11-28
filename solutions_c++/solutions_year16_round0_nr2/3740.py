#include <iostream>
#include <string>
#include <algorithm>

void reverse(std::string::iterator b, std::string::iterator e)
{
    std::reverse(b, e);
    for (;b != e; ++b) {
        *b = (*b == '+' ? '-' : '+');
    }
}

bool do_step(std::string & S)
{
    if (S.empty())
        return false;

    const char firstchar = S.front();
    size_t pos = S.find_first_not_of(firstchar);
    if (pos == std::string::npos) {
        if (firstchar == '+') {
            return false;
        } else {
            pos = S.length();
        }
    }
    reverse(S.begin(), S.begin() + pos);
    return true;
}
 

int main (int argc, char * argv[]) {
    size_t number_of_test_cases;
    std::cin >> number_of_test_cases;
    for (size_t test_case_number = 1; test_case_number <= number_of_test_cases; ++test_case_number) {
        std::string S;
        std::cin >> S;

        size_t number_of_flips = 0;
            
        while (do_step(S)) {
            ++number_of_flips;
        }
        std::cerr << "Case #" << test_case_number << ": " << number_of_flips << std::endl;
        std::cout << "Case #" << test_case_number << ": " << number_of_flips << std::endl;
    }
}