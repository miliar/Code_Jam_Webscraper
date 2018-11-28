#include <cstdint>
#include <iostream>
#include <list>
#include <string>

using namespace std;

void SolveTestCaseI(uint64_t i, const std::string& s)
{
    std::list<char> result;
    for (size_t i = 0; i < s.size(); ++i)
    {
        if (!result.size() || s[i] >= result.front())
            result.push_front(s[i]);
        else
            result.push_back(s[i]);
    }
    std::cout << "Case #" + to_string(i) << ": ";
    while (result.size())
    {
        std::cout << result.front();
        result.pop_front();
    }
    std::cout << std::endl;
}

int main()
{
    uint64_t t;
    cin >> t;
    for (uint64_t i = 1; i <= t; ++i)
    {
        std::string s;
        std::cin >> s;
        SolveTestCaseI(i, s);
    }
    return 0;
}
