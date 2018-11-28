#include <iostream>
#include <vector>
#include <string>

int solve(std::vector<int>&& levels) {
    int ans = 0;
    int currentStanding = 0;
    for (int i = 0; i < (int)levels.size(); ++i) {
        if (currentStanding >= i) {
            currentStanding += levels[i];
        } else {
            ans += (i - currentStanding);
            currentStanding = levels[i] + i;
        }
    }

    return ans;
}

std::vector<int> parseLevels(const std::string& input) {
    std::vector<int> levels(input.size());
    for (size_t i = 0; i < input.size(); ++i)
        levels[i] = input[i] - '0';
    return levels;
}

int main() {
    size_t tests;
    std::cin >> tests;
    for (size_t test = 1; test <= tests; ++test) {
        size_t max;
        std::string input;
        std::cin >> max >> input;
        std::cout << "Case #" << test << ": " <<
            solve(parseLevels(input)) << std::endl;
    }
    return 0;
}