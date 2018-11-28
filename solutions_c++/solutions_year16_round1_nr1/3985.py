#include <iostream>
#include <string>

std::string solve(const std::string& input)
{
    std::string result;
    result += input[0];

    for(auto it = input.begin() + 1; it != input.end(); ++it)
    {
        if(*it >= result.front())
        {
            result = *it + result;
        }
        else
        {
            result += *it;
        }
    }

    return result;
}

int main(int argc, char *argv[])
{
    int t;
    std::cin >> t;

    for(int i = 0; i < t; ++i)
    {
        std::string input;
        std::cin >> input;

        std::cout << "Case #" << i + 1 << ": ";
        std::cout << solve(input) << '\n';
    }
    std::cout.flush();
}
