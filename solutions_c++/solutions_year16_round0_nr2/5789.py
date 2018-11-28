#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <queue>

enum Pancake : char
{
    HAPPY = '+',
    BLANK = '-'
};

using PancakeStack = std::string;

int find_min_flips(PancakeStack pancakes);

int main(int argc, char *argv[])
{
    int t;
    std::cin >> t;
    std::cin.ignore();

    for(int i = 0; i < t; ++i)
    {
        std::string pancakes;
        std::getline(std::cin, pancakes);

        int min = find_min_flips(std::move(pancakes));
        std::cout << "Case #" << i + 1 << ": " << min << '\n';
    }

    std::cout.flush();
}

int find_min_flips(PancakeStack pancakes)
{
    int res = 0;
    char last = pancakes[0];
    for(int i = 1; i < pancakes.size(); ++i)
    {
        if(pancakes[i] != last)
        {
            res += 1;
            last = pancakes[i];
        }
    }


    if(last == '-')
    {
        for(auto& ch : pancakes)
        {
            ch = ch == HAPPY ? BLANK : HAPPY;
        }
        return 1 + find_min_flips(pancakes);
    }

    return res;
}
