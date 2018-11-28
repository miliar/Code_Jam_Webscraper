#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <numeric>
#include <array>
#include <chrono>

using int_type = unsigned long long;
using digit_map = std::array<bool, 10>;
using cache_map = std::unordered_map<int, int>;

inline void check_digits(int x, digit_map& map)
{
    // get the digits in x
    while(x > 0)
    {
        map[x % 10] = true;
        x /= 10;
    }
}

// return 0 on failure
int_type solve(int_type num)
{
    if(num == 0)
    {
        return 0;
    }

    std::vector<int> seen_nums;

    digit_map map;
    std::for_each(std::begin(map), std::end(map), [](bool& x) { x = false; });

    for (int i = 1; ; ++i)
    {
        const int_type x = num * i;

        bool finished = false;

        seen_nums.emplace_back(x);
        check_digits(x, map);

        // if we found all 10 digits
        if(std::accumulate(map.begin(), map.end(), 0) == 10)
        {
            return x;
        }
    }

    return 0;
}

int main(int argc, char *argv[])
{
    int t;
    std::cin >> t;

    for(int i = 0; i < t; ++i)
    {
        int x;
        std::cin >> x;

        std::cout << "Case #" << i + 1 << ": ";

        int result = solve(x);
        if(result == 0)
        {
            std::cout << "INSOMNIA";
        }
        else
        {
            std::cout << result;
        }
        std::cout << '\n';
    }

    std::cout.flush();
}
