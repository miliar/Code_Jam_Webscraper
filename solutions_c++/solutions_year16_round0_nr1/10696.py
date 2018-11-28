#include <iostream>
#include <fstream>

using namespace std;

int all_bits_set(int n) {
    return (n == 1023);
}

void set_bits(int *bits, int n) {
    while (n > 0) {
        int digit = (n % 10);
        *bits = *bits | (1 << digit);
        n /= 10;
    }
}

void func(long unsigned int n) {
    int bits = 0;
    for (int i = 0; ; i++) {
        long unsigned num = i * n;
        set_bits(&bits, num);
        if (all_bits_set(bits)) {
            printf("%d\n", num);
            break;
        }
    }
}

void main() {
    std::ifstream ifs;

    ifs.open("A-large.in", std::ifstream::in);

    long unsigned t, n;
    ifs >> t;
    for (int i = 1; i <= t; ++i) {
        ifs >> n;
        cout << "Case #" << i << ": ";
        if (n == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        func(n);
    }
}
