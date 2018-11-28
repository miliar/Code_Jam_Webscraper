#include <cstdio>
#include <algorithm>

int main ( void ) {
    int TA; scanf("%d", &TA);
    int cc = 1, s;
    char st[10000];
    while(TA--) {
        scanf("%d %s", &s, st);

        int len = strlen(st);
        int acc = st[0] - '0';
        int toadd = 0;

        for(int i = 1; i < len; i++) {
            int cur = st[i] - '0';

            if(acc >= i) acc += cur;
            else {
                toadd += i - acc;
                acc = acc + (i - acc) + cur;
            }
        }

        printf("Case #%d: %d\n", cc++, toadd);


    }
    


    return 0;
}
