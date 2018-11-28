#include <stdio.h>

using namespace std;

const int N = 1e3 + 5;

char digit[N];

int main() {
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.ads", "w", stdout);
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        int mmax, cur = 0, ans = 0;
        scanf("%d %s", &mmax, digit);
        for(int level = 0; level <= mmax; ++level) {
            int cnt = digit[level] - '0';
            if(level > cur) {
                ans += level - cur;
                cur += level - cur;
            }
            cur += cnt;
        }
        printf("Case #%d: %d\n", ++ncase, ans);
    }
    return 0;
}
