#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,x,r,c;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        scanf("%d%d%d", &x,&r,&c);
        int m = min(r,c);
        int n = max(r,c);
        printf("Case #%d: ", cas);
        if (x == 1) printf("GABRIEL\n");
        else if (x == 2) {
            if ( (m==1&&(n==1||n==3)) ||
                (m==3 && n==3))
                printf("RICHARD\n");
            else printf("GABRIEL\n");
        } else if (x==3) {
            if ( (m==3&&(n==3||n==4)) ||
                (m==2&&n==3) )
                printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if (x == 4) {
            if (n == 4 && (m==3 || m==4))
                printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
    }
    return 0;
}