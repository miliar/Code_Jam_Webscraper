#include <iostream>

int solve(std::string s)
{
    int res = 0;
    for (size_t i = 0; i + 1 < s.size(); ++i) {
        if (s[i] != s[i + 1]) ++res;
    }
    return res;
}

int main()
{
    int T;
    std::string s;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> s;
        std::cout << "Case #" << t << ": " << solve(s + "+") << "\n";
    }
    
    return 0;
}