#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define MAX_S 1010
char s[MAX_S];
int t, tc, c, n, d, l, i;

int main() {
    scanf("%d", &t);

    for(tc=1;tc<=t;++tc) {
        scanf("%d %s",&l,s);

        n = 0;
        c = (int) (s[0] - '0');
        for(i=1;i<=l;++i) {
            if (c<i) {
                d = i - c;
                n = n + d;
                c = c + d;
            }
            c = c + (int) (s[i]-'0');
        }

        printf("Case #%d: %d\n", tc, n);
    }
    return 0;
}
