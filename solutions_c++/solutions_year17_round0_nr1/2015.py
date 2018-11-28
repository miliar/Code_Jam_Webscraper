#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

char s[2001]; int sn;

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        int K;
        scanf("%s%d", s, &K);
        sn = strlen(s);

        bool OK = true;
        int cnt = 0;

        for (int si = 0; si < sn; si++)
            if ( s[si] == '-' ) {
                if ( si+K <= sn ) {
                    for (int Ki = 0; Ki < K; Ki++)
                        s[si+Ki] = '+'+'-'-s[si+Ki];
                    cnt++;
                } else {
                    OK = false;
                }
            }

        printf("Case #%d: ", Ti);
        if ( OK ) printf("%d\n", cnt);
        else puts("IMPOSSIBLE");
    }
}
