#include<bits/stdc++.h>
using namespace std;

char s[5555];

int main() {

    int n,k,i,j,bb,res;

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {

        scanf("%s%d", &s, &k);
        n = strlen(s);

        res = 0;
        for(i=0; i<=n-k; i++) {
            if (s[i] == '-') {
                res++;
                for(j=0; j<k; j++) {
                    s[i+j] = (s[i+j] == '-') ? '+' : '-';
                }
            }
        }

        bb = true;
        for(i=0; i<n; i++) bb = bb && (s[i] == '+');

        printf("Case #%d: ", tt);
        if (!bb) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", res);
        }
    }

    return 0;
}
