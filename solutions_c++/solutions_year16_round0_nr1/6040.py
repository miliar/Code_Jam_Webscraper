#include <iostream>
#include <string>
#include <bitset>

std::bitset<10> get_digits(int n) {
    std::bitset<10> digits;
    std::string n_str = std::to_string(n);
    for (int i = 0; i < n_str.length(); i++) {
        digits.set(n_str[i] - '0');
    }
    return digits;
}

std::string get_last_number(int n) {
    if (n == 0) {
        return "INSOMNIA";
    }
    std::bitset<10> seen_digits;
    int current_n = 0;
    while (seen_digits.count() != 10) {
        current_n += n;
        seen_digits |= get_digits(current_n);
    }
    return std::to_string(current_n);
}

int main() {
    int t, n;
    std::cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        std::cin >> n;  // read N
        std::cout << "Case #" << i << ": " << get_last_number(n) << std::endl;
    }
}
