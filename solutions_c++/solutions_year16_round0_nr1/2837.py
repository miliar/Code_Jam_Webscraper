#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

int generate_mask(int m) {
    int mask = 0;
    while (m >= 1) {
        mask |= 1 << (m % 10);
        m /= 10;
    }
    return mask;
}

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, n, m, mask;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%d", &n);
        if (n == 0)
            printf("Case #%d: INSOMNIA\n", i);
        else {
            mask = 0;
            m = n;
            while (mask != (1 << 10) - 1) {
                mask |= generate_mask(m);
                m += n;
            }
            printf("Case #%d: %d\n", i, m - n);
        }
    }
    return 0;
}
