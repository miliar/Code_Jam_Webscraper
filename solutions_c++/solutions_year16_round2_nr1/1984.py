#include <string>
#include <map>
#include <memory>
#include <iostream>
#include <unordered_map>
#include <stack>
#include <vector>
#include <cassert>
#include <algorithm>


std::string solve(const std::string& digits)
{
    std::vector<int> counter(256, 0);
    std::vector<int> ans(10, 0);

    for(const auto& x: digits)
    {
        counter[x]++;
    }

    ans.at(0) = counter.at('Z');
    counter.at('E') -= counter.at('Z');
    counter.at('R') -= counter.at('Z');
    counter.at('O') -= counter.at('Z');
    counter.at('Z') = 0;

    ans.at(2) = counter.at('W');
    counter.at('T') -= counter.at('W');
    counter.at('O') -= counter.at('W');
    counter.at('W') = 0;

    ans.at(6) = counter.at('X');
    counter.at('S') -= counter.at('X');
    counter.at('I') -= counter.at('X');
    counter.at('X') = 0;

    ans.at(7) = counter.at('S');
    counter.at('E') -= counter.at('S');
    counter.at('V') -= counter.at('S');
    counter.at('E') -= counter.at('S');
    counter.at('N') -= counter.at('S');
    counter.at('S') = 0;

    ans.at(8) = counter.at('G');
    counter.at('E') -= counter.at('G');
    counter.at('I') -= counter.at('G');
    counter.at('H') -= counter.at('G');
    counter.at('T') -= counter.at('G');
    counter.at('G') = 0;

    ans.at(3) = counter.at('H');
    counter.at('T') -= counter.at('H');
    counter.at('R') -= counter.at('H');
    counter.at('E') -= counter.at('H');
    counter.at('E') -= counter.at('H');
    counter.at('H') = 0;

    ans.at(4) = counter.at('R');
    counter.at('F') -= counter.at('R');
    counter.at('O') -= counter.at('R');
    counter.at('U') -= counter.at('R');
    counter.at('R') = 0;

    ans.at(5) = counter.at('F');
    counter.at('I') -= counter.at('F');
    counter.at('V') -= counter.at('F');
    counter.at('E') -= counter.at('F');
    counter.at('F') = 0;

    ans.at(9) = counter.at('I');
    counter.at('N') -= counter.at('I') * 2;
    counter.at('E') -= counter.at('I');
    counter.at('I') = 0;

    ans.at(1) = counter.at('E');
    counter.at('O') -= counter.at('E');
    counter.at('N') -= counter.at('E');
    counter.at('E') = 0;

    assert(std::all_of(std::begin(counter), std::end(counter),
                       [](int x)
                       { return x == 0; }));

    std::string res;
    for(int i = 0; i < 10; ++i)
    {
        for(int j = 0; j < ans.at(i); ++j)
        {
            res += '0' + i;
        }
    }

    return res;
}

int main()
{
    int n;
    std::cin >> n;

    for(int i = 1; i <= n; ++i)
    {
        std::string s;
        std::cin >> s;
        std::cout << "Case #" << i << ": " << solve(s) << std::endl;
    }

    return 0;
}