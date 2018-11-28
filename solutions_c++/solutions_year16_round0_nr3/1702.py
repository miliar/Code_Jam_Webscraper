#include <bits/stdc++.h>
#define debug(args...) fprintf(stderr, args)

using namespace std;

typedef long long lint;

void go() {
    int N, J, cnt = 0;
    scanf("%d%d", &N, &J);
    for(int i = 2; cnt < J && i < (1 << (N / 2 + 1)); i++) {
        if((i & (1 << 0)) == 0) continue;
        if((i & (1 << (N / 2 - 1))) == 0) continue;
        debug("Iniciei\n");
        vector<lint> v;
        for(int k = 2; k <= 10; k++) {
            lint base = 1, num = 0;
            for(int j = 0; j < N / 2 + 1; j++) {
                num += base * ((i & (1 << j)) != 0);
                base *= k;
            }
            debug("Deu %lld\n", num);
            v.push_back(num);
        }
        int ans = i * ((1 << ((N + 1) / 2)) + 1);
        cnt++;
        for(int k = N - 1; k >= 0; k--) printf("%d", (ans & (1 << k)) != 0);
        for(lint d : v) printf(" %lld", d);
        printf("\n");
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        debug("Entering test %d\n", i);
        printf("Case #%d:\n", i);
        go();
    }
    return 0;
}
