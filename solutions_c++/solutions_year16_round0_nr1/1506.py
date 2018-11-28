#include <cstdio>
#include <cstring>
#include <cassert>

char n_str[20];

inline int check( int * n, int len ) {
    int s = 0;
    for (int i = 0; i < len; i++) {
        s += n[i];
    }

    return s == 10 ? 1 : 0;
}

int main () {
    int c;
    int i = 0;

    assert(freopen("sheep.in", "r", stdin));
    assert(freopen("sheep.out", "w", stdout));

    scanf("%d", &c);

    while ( i++ < c ) {
        int nums[10];
        memset(nums, 0, sizeof(nums));

        long long n = 0;
        scanf("%lld", &n);

        int m = 0;
        while ( m++ < 1000 ) {
            long long temp_n  = n * m;
            do {
                int digit = temp_n % 10;
                nums[digit] = 1;
                temp_n /= 10;
            } while ( temp_n > 0 );

            if ( check(nums, 10) ) {
                n = n * m;
                m = -1;
                break;
            }
        }

        if (m == -1) {
            printf("Case #%d: %lld\n", i, n);
        } else{
            printf("Case #%d: INSOMNIA\n", i);
        }
    }

    return 0;
}
