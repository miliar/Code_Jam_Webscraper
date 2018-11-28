#include <cstdio>
#include <cstdlib>
#include <cstring>

#define N 16
#define J 50

#define P_MAX 100000000

unsigned int MIN, MAX;

int prime[5761455], P = 0;
int pf[P_MAX];

unsigned int long long jamcoins[J], found = 0;

void init() {
    for (int i = 1; i < P_MAX; i++) pf[i] = i;
    for (int i = 2; i < P_MAX; i++) if (pf[i] == i) {
        prime[P++] = i;
        for (int j = i + i; j < P_MAX; j += i) {
            pf[j] = i;
        }
    }
}

int is_prime(long long n) {
    for (int i = 0; i * i < n && i < P; i++) {
        if (n % prime[i] == 0) {
            return 0;
        }
    }
    return 1;
}

void print_binary(unsigned int coin) {
    int j;
    char c[64];
    for (j = 0; j < 64 && coin; j++) {
        c[j] = coin & 1 ? '1' : '0';
        coin >>= 1;
    }
    for (j = j - 1; j >= 0; j--) {
        putchar(c[j]);
    }
}

long long value_in_base(unsigned int coin, int base) {
    long long value = 0, r = 1;
    while (coin) {
        if (coin & 1) {
            value += r;
        }
        r *= base;
        coin >>= 1;
    }
    return value;
}

int is_valid_in_base(unsigned int coin, int base) {
    long long value = value_in_base(coin, base);
    return !is_prime(value);
}

int is_jamcoin(unsigned int coin) {
    for (int base = 2; base <= 10; base++) {
        if (!is_valid_in_base(coin, base)) {
            return 0;
        }
    }
    return 1;
}

int repeated(unsigned int coin) {
    for (int i = 0; i < found; i++) {
        if (coin == jamcoins[i]) {
            return 1;
        }
    }
    return 0;
}

int find_divisor(int coin, int base) {
    long long value = value_in_base(coin, base);
    for (long long i = 2; i < value; i++) if (i != base) {
        if (value % i == 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    MIN = (1 << (N - 1)) + 1;
    MAX = (1 << N) - 1;

    init();

    puts("Case #1:");
    while (found < J) {
        unsigned int coin = (rand() & MAX) | MIN;
        if (!is_jamcoin(coin) || repeated(coin)) {
            continue;
        }

        print_binary(coin);
        for (int base = 2; base <= 10; base++) {
            printf(" %d", find_divisor(coin, base));
        }
        puts("");
        jamcoins[found++] = coin;
    }

    return 0;
}
