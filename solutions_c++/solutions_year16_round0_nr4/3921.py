#include <cstdio>

typedef long long int lld;
lld K, C, S;

int main() {

    lld cases;
    scanf("%lld", &cases);
    for (lld test=1; test<=cases; ++test) {
        scanf("%lld %lld %lld", &K, &C, &S);

        lld KC = 1;
        for (lld i=1; i<=C-1; ++i)
            KC *= K;

        printf("Case #%lld: ", test);
        for (lld i=1; i<=S; ++i) {
            lld num = KC;
            lld ans = 0;
            while (num > 1) {
                ans += num * (i-1);
                num /= K;
            }
            ans += i;
            printf("%lld ", ans);
        }
        printf("\n");
    }

    return 0;

}
