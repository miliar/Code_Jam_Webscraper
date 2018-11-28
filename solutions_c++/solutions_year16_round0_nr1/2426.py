#include <iostream>
#include <limits>
#include <set>
#include <string>

std::string insomnia("INSOMNIA");

void InsertDigits(int64_t n, std::set<int64_t>& seenDigits)
{
    while (n > 0) {
        int64_t digit = n % 10;
        seenDigits.insert(digit);
        n /= 10;
    }
}

std::string CountingSheep(int64_t n) {
    if (n == 0) {
        return std::string("INSOMNIA");
    } else {
        std::set<int64_t> seenDigits;
        int64_t max = std::numeric_limits<int64_t>::max();
        int64_t current = n;
        while (current < max - n) {
            InsertDigits(current, seenDigits);
            if (seenDigits.size() == 10) {
                return std::to_string(current);
            }
            current += n;
        }
        return std::string("INSOMNIA");
    }
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; i++) {
        int n;
        std::cin >> n;
        std::cout << "Case #" << i << ": ";
        std::cout << CountingSheep(n) << std::endl;
    }

    return 0;
}