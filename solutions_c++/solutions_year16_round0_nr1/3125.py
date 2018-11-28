/* Author: Ankit Sultana
 * * * * * * * * * * * */
#include <stdio.h>
#define LL long long
#define MAXN 1000003

bool checker(bool vis[]) {
    for(int i = 0; i < 10; i++) {
        if(! vis[i])    return false;
    }
    return true;
}

void go(int x, bool vis[]) {
    while(x) {
        vis[x%10] = true;
        x /= 10;
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tc = 1; tc <= t; tc++) {
        printf("Case #%d: ", tc);
        bool vis[10] = {false};
        LL n;
        scanf("%lld", &n);
        if(n == 0) {
            printf("INSOMNIA\n");
        } else {
            LL i;
            for(i = n; ; i+=n) {
                go(i, vis);
                if(checker(vis))    break;
            }
            printf("%lld\n", i);
        }
    }
    return 0;
}
