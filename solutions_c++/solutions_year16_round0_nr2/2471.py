#include <iostream>
#include <string>

int PancakeFlips(const std::string& s) {
    if (s.empty()) {
        return 0;
    }

    int flips = 0;
    char previous = s[0];
    for (size_t i = 1; i < s.length(); i++) {
        char current = s[i];
        if (current != previous) {
            flips++;
            previous = current;
        }
    }

    if (s.back() != '+') {
        flips++;
    }

    return flips;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; i++) {
        std::string s;
        std::cin >> s;
        std::cout << "Case #" << i << ": ";
        std::cout << PancakeFlips(s) << std::endl;
    }

    return 0;
}