#include <stdio.h>
#include <stdlib.h>

const int N = 1000+10;

char s[N];

int main(){
    int T, n, i, ans, tmp;
//
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);


    scanf("%d", &T);
    for (int tcase=1; tcase<=T; tcase++) {
        scanf("%d%s", &n, s);
        //
        ans = tmp = 0;
        for (i=0; i<=n; i++) {
            if (tmp<i) {
                ans += (i-tmp);
                tmp = i;
            }
            tmp += s[i]-'0';
        }
        printf("Case #%d: %d\n", tcase, ans);
    }

    return 0;
}
