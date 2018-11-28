#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int nn;
long long n, m, x, y;

long long f(){
    long long t = 1, e = 0, re = 0;
    for (int i = 0;i < nn;i++){
        if (e >= m) return re;
        e |= (1ll<<(nn - i - 1));
        re += t;
        t <<= 1;
    }
    return m;
}

void init(){
    scanf("%d%lld", &nn, &m);
}

void work(){
    n = 1ll<<nn;
    x = f();
    m = n - m;
    y = f();
}

int main(){
#ifdef LATTE
//    freopen("b.in", "r", stdin);
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
//    freopen("out.txt", "w", stdout);
#endif
    int T, t = 1;
    scanf("%d", &T);
    while (T--){
        init();
        work();
        printf("Case #%d: %lld %lld\n", t++, x - 1, n - y - 1);
    }
    return 0;
}
