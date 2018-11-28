#include <iostream>
#include <string>

long solve(char sign, const std::string &s, size_t length)
{
    if (length == 0)
        return 0;
    else if (length == 1) {
        if (s[0] == sign)
            return 0;
        else
            return 1;
    } else {
        if (s[length-1] == sign) {
            return solve(sign, s, length-1);
        } else {
            return 1 + solve(sign == '+' ? '-':'+', s, length-1);
        }
    }
}

int main()
{
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::string s;
        std::cin >> s;
        std::cout << "Case #" << i << ": ";
            std::cout << solve('+', s, s.size());
        std::cout << '\n';
    }
    return 0;
}
