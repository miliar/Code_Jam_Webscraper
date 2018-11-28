#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

long findDivisor(long n) {
    if (n % 3 == 0) {
        return 3;
    }

    if (n % 5 == 0) {
        return 5;
    }

    if (n % 7 == 0) {
        return 7;
    }

    long i = 11;
    while (i * i <= n) {
        if (n % i == 0) {
            return i;
        }
        else if (n % (i + 2) == 0) {
            return i + 2;
        }

        i += 6;
    }

    return 1;
}

int main(int argc, char const *argv[])
{
    int N = 16, J = 50;
    long coin[11], nextCoin;
    long divisor[11];

    for (int i = 2; i <= 10; ++i) {
        coin[i] = (long) pow(i, N - 1) + 1;
    }

    printf("Case #1:\n");

    while (J > 0) {
        bool isPrime = false;
        int d = 1;

        for (int i = 2; i <= 10; ++i) {
            if (!isPrime) {
                divisor[i] = findDivisor(coin[i]);
                if (divisor[i] == 1) {
                    isPrime = true;
                }
            }
        }

        if (!isPrime) {
            J--;

            printf("%ld ", coin[10]);
            for (int i = 2; i < 10; ++i) {
                printf("%ld ", divisor[i]);
            }
            printf("%ld\n", divisor[10]);
        }

        if (J == 0) continue;

        coin[2] += 2;
        for (int i = 3; i <= 10; ++i) {
            coin[i] = 1;
        }
        while (d < N) {
            if ((1 << d) & coin[2]) {
                for (int i = 3; i <= 10; ++i) {
                    coin[i] += (long) pow(i, d);
                }
            }
            d++;
        }
    }

    return 0;
}
