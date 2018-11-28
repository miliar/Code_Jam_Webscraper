#include <iostream>
#include <array>
#include <algorithm>
#include <string>

int solve(std::string stack)
{
    int n = 0;
    char c = '+';
    for (auto it = stack.rbegin(); it != stack.rend(); ++it) {
        char next = *it;
        if (c != next) {
            c = next;
            ++n;
        }
    }
    return n;
}

int main()
{
    int numCases;
    std::cin >> numCases;

    int i = 0;
    std::string stack;
    while (++i, std::cin >> stack) {

        int solution = solve(stack);
        std::cout << "Case #" << i << ": " << solution << std::endl;
    }

    return 0;
}

