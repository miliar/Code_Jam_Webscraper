#include <bits/stdc++.h>

#define DEBUG 1

using namespace std;

#if DEBUG
    FILE* input = fopen("input.txt", "r");
    FILE* output = fopen("output.txt", "w");
    #define scanf(...) fscanf(input, __VA_ARGS__)
    #define printf(...) fprintf(output, __VA_ARGS__)
#endif // DEBUG

typedef unsigned long long ull;

int divisor[100005];

ull bitSetToNum(ull bitSet, int base) {
    ull res = 0;
    ull test = 1;
    ull pow = 1;

    for (int i = 0; i <= 32; i++) {
        if (bitSet & test) {
            res += pow;
        }
        pow *= base;
        test <<= 1;
    }
    return res;
}

uint64_t modMul(uint64_t a, uint64_t b, uint64_t c)
{
	uint64_t x = 0;
	while (b != 0) {
		if (b % 2 == 1) {
			x = (x + a) % c;
		}
		a = (a + a) % c;
		b /= 2;
	}
	return x % c;
}

uint64_t modularPow(uint64_t a, uint64_t x, uint64_t mod) {
    uint64_t r = 1;

    while (x) {
        if ((x & 1) == 1) {
            r = modMul(a, r, mod);
        }
        x >>= 1;
        a = modMul(a, a, mod);
    }
    return r;
}

uint64_t rand_between(uint64_t a, uint64_t b) {
    uint64_t r = ((uint64_t)(rand()) << 32) | rand();
    return a + (uint64_t)((double)(b - a + 1)*r/(UINT64_MAX + 1.0));
}

bool isPrime(uint64_t n, int k) {
    if (n==2 || n==3) {
        return true;
    }
    if (n <= 1 || !(n & 1)) {
        return false;
    }

    int s = __builtin_ctzll(n - 1);
    uint64_t d = (n-1)/(1 << s);

    for (int i = 0; i < k; ++i) {
        uint64_t a = rand_between(2, n - 2);
        uint64_t x = modularPow(a, d, n);

        if (x == 1 || x == n-1) {
            continue;
        }

        for (int r = 1; r < s; ++r) {
            x = modularPow(x, 2, n);
            if ( x == 1 ) {
                return false;
            }

            if ( x == n - 1 ) {
                goto LOOP;
            }
        }

        return false;

        LOOP:
            continue;
    }
    return true;
}

ull findDiv(ull num) {
    for (ull i = 2; i < num; i++) {
        if (num % i == 0) {
            return i;
        }
    }
    return 0; //assume this won't happen
}

int main()
{
    srand(time(NULL));

    ull firstAndLastSet = (1 << 15) | (1);
    ull curNum = 0;

    int found = 0;

    while (found < 50) {
        curNum++;
        ull curBitSet = firstAndLastSet | (curNum << 1);

        bitset<16> convertToStr(curBitSet);
        vector<ull> divisors;

        for (int i = 2; i <= 10; i++) {
            ull num = bitSetToNum(curBitSet, i);

            if (!isPrime(num, 10)) {
                divisors.push_back(findDiv(num));
            } else {
                goto nextIt;
            }
        }

        printf("%s", convertToStr.to_string().c_str());
        for (ull divis : divisors) {
            printf(" %llu", divis);
        }
        printf("\n");
        found++;

nextIt:
    ;// do nothing
    }

    return 0;
}
