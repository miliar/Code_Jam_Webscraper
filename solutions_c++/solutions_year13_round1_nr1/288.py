#include <cstdio>
using namespace std;

long long r0, t0;

int main(void) {
    int T;
    scanf("%d", &T);
    for(int ti = 1; ti <= T; ti++) {
        printf("Case #%d: ", ti);

        scanf("%I64d %I64d", &r0, &t0);
        long long used = 0;
        long long r = r0;
        int y = 0;

        while(used + 2*r+1 <= t0) {
            used += 2*r+1;
            y++;
            r+=2;
        }
        printf("%d\n", y);

    }
    return 48-48;
}
