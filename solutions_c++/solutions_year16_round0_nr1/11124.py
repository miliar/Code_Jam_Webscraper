#include <iostream>
#include <array>

long long run();

int main() {
    // Speed up io.
    std::ios_base::sync_with_stdio(false);

    // Number of tests.
    long long t; std::cin >> t;

    for (int i = 1; i <= t; ++i) {
        std::cout   << "Case #" << i << ": ";

        long long ans = run();

        if (ans)    std::cout << ans;
        else        std::cout << "INSOMNIA";

        std::cout << '\n';
    }

    return 0;
}

bool complete(std::array<bool, 10>& digits) {
    for (bool i : digits) if (!i) return false;

    return true;
}

long long run() {
    std::array<bool, 10> digits = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    long long N; std::cin >> N;
    long long n = N;

    // Case: 0 never changes.
    if (N == 0) return 0;

    for (int i = 1; !complete(digits); ++i) {
        for (long long x = n; x > 0; x /= 10) digits[x % 10] = true;
        n += N;
    }

    return n - N;
}
