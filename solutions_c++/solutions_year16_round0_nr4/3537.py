#include <stdio.h>
long long spow(int k, int c) {
    long long res = 1;
    for(int i=0; i<c; i++) res*=k;
    return res;
}
int main() {
    int t, k, c, s;
    scanf("%d", &t);
    for(int ii=1; ii<=t; ii++) {
        scanf("%d %d %d", &k, &c, &s);
        long long x = spow(k,c-1);
        printf("Case #%d: ", ii);
        for(int i=0; i<k; i++) {
            printf("%lld ", x*i+1);
        }
        puts("");
    }
}
