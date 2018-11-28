#include <iostream>
#include <string>

int solve(std::string const& s) {
    char current = s[0];
    int total = 1;
    for (const auto& c : s) {
        if (c != current) {
            ++total;
            current = c;
        }
    }

    if (s[s.size() - 1] == '+') --total;

    return total;
}

int main() {
    int t = 0;
    std::cin >> t;
    for (int test = 1; test <= t; ++test) {
        std::string s;
        std::cin >> s;
        auto res = solve(s);
        std::cout << "Case #" << test << ": " << res << std::endl;
    }
    return 0;
}