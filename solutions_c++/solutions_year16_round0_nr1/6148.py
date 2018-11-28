#include <iostream>
#include <algorithm>

long solve(int n)
{
    bool value[10];
    std::fill(std::begin(value), std::end(value), false);
    for (int i = 1; ; ++i) {
        const long k0 = i * n;
        auto k = k0;
        while (k>0) {
            value[k%10] = true;
            k /= 10;
        }
        if (std::all_of(std::begin(value), std::end(value),
                    [](bool b){return b;})) {
                return k0;
        }
    }
    return -1;
}


int main()
{
    int t=1000000;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        int n = i;
        std::cin >> n;
        std::cout << "Case #" << i << ": ";
        if (n == 0) {
            std::cout << "INSOMNIA";
        } else {
            std::cout << solve(n);
        }
        std::cout << '\n';
    }
    return 0;
}
