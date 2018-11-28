#include <stdio.h>
#include <algorithm>
using namespace std;
typedef long long LL;

int n;

void solve() {
    int ss = 0;
    for (LL i = 1; i <= 1000000; i++) {
        LL t = n * i;
        do {
            ss |= 1 << (t % 10);
            t /= 10;
        } while (t > 0);
        if (ss == (1<<10) - 1) {
            printf("%I64d\n",n*i);
            return ;
        }
    }
    printf("INSOMNIA\n");
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas;
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ ca) {
        scanf("%d",&n);
        printf("Case #%d: ",ca);
        solve();
    }
    return 0;
}
