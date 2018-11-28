#include <iostream>
#include <cassert>

int solve(int a)
{
    int was = 0;
    int last = 0;
    while (was != (1 << 10) - 1) {
        last += a;
        int b = last;
        while (b > 0) {
            int r = b % 10;
            was |= (1<<r);
            b /= 10;
        }
        assert(last < 100000000);
    }
    return last;
}

int main()
{
    int T, n;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> n;
        std::cout << "Case #" << t << ": ";
        if (n == 0) std::cout << "INSOMNIA\n";
        else std::cout << solve(n) << "\n";
    }
}