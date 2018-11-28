#include <stdio.h>
#include <memory.h>
#define maxf(a,b) ((a)>(b)?(a):(b))
#define minf(a,b) ((a)<(b)?(a):(b))
int cnt [10];

int main() {
    int T; scanf ("%d",&T); for (int test = 1; test <= T; test ++) {
        long long N;
        scanf ("%lld",&N);
        if (N == 0) {
            printf ("Case #%d: INSOMNIA\n", test);
            continue;
        }
        memset(cnt, 0, sizeof cnt);
        for (int i=1;;i++) {
            long long val = N * (long long) i;
            while (val > 0) {
                cnt [ val%10 ] = 1;
                val /= 10;
            }
            
            int count = 0;
            for (int j=0;j<10;j++) if(cnt[j]) count ++;
            if (count == 10) {
                printf ("Case #%d: %lld\n", test, N * (long long) i);
                break;
            }
        }
    }
    return 0;
}
