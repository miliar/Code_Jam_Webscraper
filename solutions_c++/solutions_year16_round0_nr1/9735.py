#include <cstring>
#include <iostream>

int solve(int start) {
    bool seen[10];
    memset(seen, 0, sizeof seen);
    int total = 0;
    for (int i = 1;;++i) {
        int current = start * i;
        if (current < start) throw "Overflow";
        int last = current;

        while (current) {
            int digit = current % 10;
            if (!seen[digit]) {
                ++total;
                if (total == 10) return last;
                seen[digit] = true;
            }
            current /= 10;
        }
    }

    throw "Unreachable";
}

int main() {
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n;
        std::cin >> n;
        std::cout << "Case #" << t << ": ";
        if (n == 0) {
            std::cout << "INSOMNIA" << std::endl;
        } else {
            std::cout << solve(n) << std::endl;
        }
    }

    return 0;
}