#include<cstdio>

int main() {
    
    int T;
    scanf("%d", &T);
    for(int ca=1; T--; ca++) {
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", ca);
        for(int i=1; i<=k; i++)
            printf(" %d", i);
        puts("");
    }
    return 0;
}
