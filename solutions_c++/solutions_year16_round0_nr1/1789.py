#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include <cassert>

#define dbg(...) fprintf(stderr, __VA_ARGS__)

void solve(uint64_t N) {
    uint32_t seen = 0; // bitmask, care of bits 0 to 9
    char s[50];

    dbg("Solving for %lu\n", N);

    if (N == 0) {
        printf("INSOMNIA\n");
        return;
    }

    uint64_t n;
    for (n = N; seen != 0x3ff; n += N) {
        sprintf(s, "%lu", n);
        for (char *c=s; *c != 0; c++) {
            assert('0' <= *c && *c <= '9');
            seen |= 1U << (*c - '0');
        }
        assert(seen <= 0x3ff);
        if (seen == 0x3ff) {
            printf("%lu\n", n);
            return;
        }
        if (n & (3ULL<<62))  dbg("Ehm... %lu\n", n);
    }
}

int main() {
    int T, N;
    scanf("%d", &T);
    for (int t=0; t<T; t++) {
        scanf("%d", &N);
        printf("Case #%d: ", t+1);
        solve(N);
    }
}
