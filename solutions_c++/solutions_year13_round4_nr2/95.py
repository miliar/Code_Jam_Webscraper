#include <stdio.h>
int nn;
long long n, m;
long long f(){
    long long t = 1, tt = 0, re = 0;
    for (int i = nn - 1; i >= 0; i--){
        if (tt >= m) return re;
        tt |= (1ll<<i);
        re += t;
        t <<= 1;
    }
    return m;
}
int main(){
    int T, ri = 1;
    long long x, y;
    freopen("B-large(2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%lld", &nn, &m);
        n = 1ll<<nn;
        x = f();
        m = n - m;
        y = f();
        printf("Case #%d: %lld %lld\n", ri++, x - 1, n - y - 1);
    }
    return 0;
}
