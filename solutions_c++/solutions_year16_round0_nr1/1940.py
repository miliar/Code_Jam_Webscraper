#include <bits/stdc++.h>
#define debug(args...) //fprintf(stderr, args)

using namespace std;
typedef long long lint;

void go() {
    lint n;
    int mask = 0, i;
    scanf("%lld", &n);
    for(i = 1; mask != (1 << 10) - 1; i++) {
        lint m = n * i;
        int last = mask;
        while(m) {
            mask |= (1 << (m % 10));
            m /= 10;
        }
        if(mask == 0) break;
    }
    if(mask == (1 << 10) - 1) printf("%lld\n", n * (i - 1));
    else printf("INSOMNIA\n");
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        debug("Entering Test %d\n", i);
        printf("Case #%d: ", i);
        go();
    }
    return 0;
}
