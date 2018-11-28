#include <iostream>
#include <array>
#include <algorithm>

int solve(int n)
{
    if (n == 0)
        return -1;

    std::array<bool, 10> seen;
    std::fill(seen.begin(), seen.end(), false);

    int count = 0;
    while (!std::all_of(seen.begin(), seen.end(), [](bool b) { return b; })) {
        count += n;

        for (int digits = count; digits != 0; digits /= 10) {
            int digit = digits % 10;
            seen[digit] = true;
        }
    };

    return count;
}

int main()
{
    int numCases;
    std::cin >> numCases;

    int i = 0, n;
    while (++i, std::cin >> n) {
        int solution = solve(n);
        std::cout << "Case #" << i << ": ";
        
        if (solution < 0)
            std::cout << "INSOMNIA";
        else
            std::cout << solution;
        
        std::cout << std::endl;
    }
    return 0;
}

