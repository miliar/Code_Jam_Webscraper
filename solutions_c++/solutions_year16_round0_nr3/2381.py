#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define LL long long
#define N 11

LL convert(int mask, LL base) {
    LL ret = 0, factor = 1;
    while (mask) {
        if (mask & 1)
            ret += factor;
        factor *= base;
        mask >>= 1;
    }
    return ret;
}

int not_prime(LL integer) {
    if (integer % 2 == 0)
        return 2;
    int end = std::min(100000, int(sqrt(integer)));
    for (int i = 3; i < end; i += 2) {
        if (integer % i == 0)
            return i;
    }
    return -1;
}

void print_mask(int mask) {
    char words[17];
    for (int i = 0; i < 16; ++i) {
        words[15 - i] = '0' + (mask % 2);
        mask >>= 1;
    }
    words[16] = '\0';
    printf("%s", words);
}

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, n, m;
    int bases[N];
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%d%d", &n, &m);
        printf("Case #%d:\n", i);
        for (int i = 0; i < (1 << 14); ++i) {
            int mask = i | (1 << 14);
            mask <<= 1;
            mask += 1;
            bool flag = true;
            for (int base = 2; base <= 10; ++base) {
                bases[base] = not_prime(convert(mask, base));
                if (bases[base] == -1){
                    flag = false;
                    break;
                }
            }
            if (flag) {
                print_mask(mask);
                for (int j = 2; j <= 10; ++j)
                    printf(" %d", bases[j]);
                puts("");
                --m;
                if (m == 0)
                    break;
            }
        }
    }
    return 0;
}
