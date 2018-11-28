#include <bits/stdc++.h>

using namespace std;

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T; scanf("%d", &T);
    char s[2048];
    int cnt[32];
    int dig[10];

    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%s", s);
        int len = strlen(s);
        memset(cnt, 0, sizeof(cnt));
        for(int i=0; i<len; i++) cnt[ s[i]-'A' ]++;

        memset(dig, 0, sizeof(dig));

        dig[0] = cnt[ 'Z'-'A' ];
        cnt[ 'E'-'A' ] -= cnt[ 'Z'-'A' ];
        cnt[ 'R'-'A' ] -= cnt[ 'Z'-'A' ];
        cnt[ 'O'-'A' ] -= cnt[ 'Z'-'A' ];

        dig[2] = cnt[ 'W'-'A' ];
        cnt[ 'T'-'A' ] -= cnt[ 'W'-'A' ];
        cnt[ 'O'-'A' ] -= cnt[ 'W'-'A' ];

        dig[4] = cnt[ 'U'-'A' ];
        cnt[ 'F'-'A' ] -= cnt[ 'U'-'A' ];
        cnt[ 'O'-'A' ] -= cnt[ 'U'-'A' ];
        cnt[ 'R'-'A' ] -= cnt[ 'U'-'A' ];

        dig[6] = cnt[ 'X'-'A' ];
        cnt[ 'S'-'A' ] -= cnt[ 'X'-'A' ];
        cnt[ 'I'-'A' ] -= cnt[ 'X'-'A' ];

        dig[1] = cnt[ 'O'-'A' ];
        cnt[ 'N'-'A' ] -= cnt[ 'O'-'A' ];
        cnt[ 'E'-'A' ] -= cnt[ 'O'-'A' ];

        dig[3] = cnt[ 'R'-'A' ];
        cnt[ 'T'-'A' ] -= cnt[ 'R'-'A' ];
        cnt[ 'H'-'A' ] -= cnt[ 'R'-'A' ];
        cnt[ 'E'-'A' ] -= 2*cnt[ 'R'-'A' ];

        dig[5] = cnt[ 'F'-'A' ];
        cnt[ 'I'-'A' ] -= cnt[ 'F'-'A' ];
        cnt[ 'V'-'A' ] -= cnt[ 'F'-'A' ];
        cnt[ 'E'-'A' ] -= cnt[ 'F'-'A' ];

        dig[7] = cnt[ 'S'-'A' ];
        cnt[ 'E'-'A' ] -= 2*cnt[ 'S'-'A' ];
        cnt[ 'V'-'A' ] -= cnt[ 'S'-'A' ];
        cnt[ 'N'-'A' ] -= cnt[ 'S'-'A' ];

        dig[8] = cnt[ 'T'-'A' ];
        cnt[ 'E'-'A' ] -= cnt[ 'T'-'A' ];
        cnt[ 'I'-'A' ] -= cnt[ 'T'-'A' ];
        cnt[ 'G'-'A' ] -= cnt[ 'T'-'A' ];
        cnt[ 'H'-'A' ] -= cnt[ 'T'-'A' ];

        dig[9] = cnt[ 'E'-'A' ];

        printf("Case #%d: ", ncase);
        for(int i=0; i<10; i++) {
            for(int j=0; j<dig[i]; j++)
                printf("%d", i);
        }
        printf("\n");
    }

    return 0;
}
