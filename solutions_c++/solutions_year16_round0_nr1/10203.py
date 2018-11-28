#include <iostream>
#include <unordered_set>
#include <string>


long long can_sleep(long long N) {
    long long counter = 2;
    long long number = N;
    std::unordered_set<char> digit_set;
    while(true) {
        if (digit_set.size() == 10) {
            return number;
        }
        auto word = std::to_string(number);
        for (auto x : word) {
            digit_set.insert(x);
            if (digit_set.size() == 10) {
                return number;
            }
        }
        number = N * counter;
        counter += 1;
    }
    if (digit_set.size() != 10) {
        return -1;
    }
    return number;
}

int main() {
    int T;
    std::cin >> T;
    long long N;
    for(int i = 0; i < T; ++i) {
        std::cin >> N;
        if (N == 0) {
            std::cout << "Case #" << (i+1) << ": " << "INSOMNIA\n";
        } else {
            auto res = can_sleep(N);
            if (res <= 0) {
            std::cout << "case #" << (i+1) << ": " << "insomnia\n";
            } else {
            std::cout << "case #" << (i+1) << ": " << res << '\n';
            }
        }
    }
}
