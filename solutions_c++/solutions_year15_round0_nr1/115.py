#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int N, M;
char str[5005];
int main(){
    int T, i, ca;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int s;
        scanf("%d%s", &s, str);
        int r = 0;
        int t = 0;
        for (int i = 0; i <= s; ++i) {
            if (t < 0) {
                ++r;
                ++t;
            }
            --t;
            t += str[i] - '0';
        }
        printf("Case #%d: %d\n", ca, r);
    }
    return 0;
}
