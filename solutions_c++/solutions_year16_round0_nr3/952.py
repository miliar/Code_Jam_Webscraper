// Written by Luis Garcia, 2016.
// OJ-ID: CJ1601C

#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <algorithm>

using namespace std;

static const uint64_t BIGINT_BASE = 1000000;

void convertToBase(uint64_t n, uint64_t b, uint64_t * s) {
    uint64_t h[10] = {1};

    for (uint64_t r = n; r != 0; r /= 2) {
        uint64_t sh = 0;
        for (int i = 0; i < 10; ++i) {
            sh += r % 2 * h[i] + s[i];
            s[i] = sh % BIGINT_BASE;
            sh /= BIGINT_BASE;
        }

        uint64_t rh = 0;
        for (int i = 0; i < 10; ++i) {
            rh += h[i] * b;
            h[i] = rh % BIGINT_BASE;
            rh /= BIGINT_BASE;
        }
    }
}

int main() {
    int T, N, J;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d %d", &N, &J);

        printf("Case #%d:\n", _T);

        uint32_t samples = 1U << (N - 2);
        uint32_t mask = (1U << (N - 1)) | 1;

        for (int i = 0; J > 0 && i < samples; ++i) {
            uint32_t n = (i << 1) | mask;

            bool hasPrime = false;

            uint64_t div[11] = {};
            for (uint32_t base = 2; !hasPrime && base <= 10; ++base) {
                bool valid = false;

                uint64_t s[10] = {};
                convertToBase(n, base, s);
                for (uint64_t p = 2; !valid && p <= 5000; ++p) {
                    uint64_t r = 0;
                    for (int f = 9; f >= 0; --f) r = (r + s[f]) % p * BIGINT_BASE;
                    if (r == 0) div[base] = p, valid = true;
                }
                if (!valid) hasPrime = true;
            }

            if (!hasPrime) {
                char sz[40];
                itoa(n, sz, 2);

                printf("%s", sz);
                for (uint32_t base = 2; base <= 10; ++base)
                    printf(" %llu", div[base]);
                printf("\n");
                --J;
            }
        }
    }

    // printf("%d\n", J);

    return 0;
}
