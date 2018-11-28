#include <iostream>

int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        std::cin >> n;

        std::cout << "Case #" << i + 1 << ": ";

        if (n == 0) {
            std::cout << "INSOMNIA\n";
            continue;
        }

        int digits = 0;
        int m = 0;
        do {
            m++;
            int k = n * m;
            while (k > 0) {
                digits |= 1 << (k % 10);
                k /= 10;
            }
        } while (digits != 0x3ff);

        std::cout << n * m << "\n";
    }
}
