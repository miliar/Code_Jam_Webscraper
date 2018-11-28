#include <cstdio>
#include <cstdlib>

using namespace std;

long long get_divisor(long long num) {
    for (long long x = 2; x * x <= num; x++) {
        if (num % x == 0)
            return x;
    }
    return 0;
}

long long get_num(bool jamcoin[], int base) {
    long long res = 0, z = 1;
    for (int i = 15; i >= 0; i--) {
        res += z * jamcoin[i];
        z *= base;
    }
    return res;
}

bool get_divisors(bool jamcoin[], long long output[]) {
    /*for (int i = 0; i < 16; i++) {
        putchar(jamcoin[i] + '0');
    }
    putchar('\n');
    printf("%lld\n\n", get_num(jamcoin, 10));*/
    for (int b = 2; b <= 10; b++) {
        long long num = get_num(jamcoin, b);
        output[b] = get_divisor(num);
        if (!output[b])
            return false;
    }
    return true;
}

int main() {
    bool jamcoin[16];
    jamcoin[0] = jamcoin[15] = true;
    long long divs[11];
    srand(1234);
    printf("Case #1:\n");
    
    for (int i = 0; i < 50; i++) {
        do {
            int r = rand();
            for (int j = 1; j < 15; j++) {
                jamcoin[j] = r & 1;
                r >>= 1;
            }
        } while (!get_divisors(jamcoin, divs));
        printf("%lld", get_num(jamcoin, 10));
        for (int j = 2; j <= 10; j++) {
            printf(" %lld", divs[j]);
        }
        printf("\n");
    }
    
    return 0;
}
