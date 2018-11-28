#include <iostream>
#include <string>

size_t solve(const std::string &levels)
{
    size_t needed = 0, active = 0;
    for (size_t i = 0; i < levels.length(); ++i) {
        size_t extra = (size_t)std::max(0, (int)i - (int)active);
        active += extra;
        needed += extra;
        active += levels[i] - '0';
    }
    return needed;
}

int main()
{
    size_t test_cases;
    std::cin >> test_cases;
    for (size_t i = 1; i <= test_cases; ++i) {
        size_t max_level;
        std::string num_people;
        std::cin >> max_level >> num_people;
        std::cout << "Case #" << i << ": " << solve(num_people) << std::endl;
    }
}