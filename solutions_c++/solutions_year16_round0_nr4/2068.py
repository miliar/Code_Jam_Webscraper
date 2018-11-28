#include <iostream>
#include <vector>
#include <algorithm>


uint64_t ipow(uint64_t base, uint64_t exp)
{
    uint64_t result = 1;
    while (exp != 0)
    {
        if ((exp & 1) == 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

std::vector<uint64_t> solve(unsigned k, unsigned c, unsigned s)
{
    std::vector<uint64_t> solution;
    unsigned count = k / c + (k % c != 0);
    
    if (s < count)
        return solution;
    
    solution.reserve(count);
    for (unsigned i = 0; i < count; ++i) {
        uint64_t check = 0;
        for (unsigned level = i * c; level < (i * c) + c; ++level) {
            unsigned branch = std::min(k-1, level);
            unsigned raise = c - (level % c) - 1;
            check += branch * ipow(k, c - (level % c) - 1);
        }
        
        solution.push_back(check);
    }
    
    return solution;
}

int main()
{
    unsigned numCases;
    std::cin >> numCases;

    unsigned k; // size
    unsigned c; // complexity
    unsigned s; // students

    uint64_t i = 0;
    std::string stack;
    while (++i, std::cin >> k >> c >> s) {
        std::vector<uint64_t> solution = solve(k, c, s);

        std::cout << "Case #" << i << ":";
        if (solution.size() > 0)
            for (uint64_t i : solution) std::cout << " " << (i + 1);
        else
            std::cout << " IMPOSSIBLE";
        std::cout << std::endl;
    }

    return 0;
}

