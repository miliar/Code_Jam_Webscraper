#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

typedef __int64 LL;

bool yoooo[10];

void puwapuwa(LL x) {
    while(x) {
        int tmp = (int)(x % 10);
        yoooo[tmp] = true;
        x = x / 10;
    }
}

bool laaaaaaa() {
    for(int i = 0; i < 10; i++) if(!yoooo[i]) return false;
    return true;
}

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    LL n, x;
    int cas = 0, t;
    scanf("%d", &t);
    bool nya;
    while(t--) {
        cas++;
        printf("Case #%d: ", cas);
        scanf("%I64d", &n);
        if(n == 0) {
            puts("INSOMNIA");
            continue;
        }
        nya = false;
        memset(yoooo, 0, sizeof yoooo);
        x = n;
        for(int i = 2; i <= 101; i++) {
            puwapuwa(x);
            if(laaaaaaa()) {
                nya = true;
                printf("%I64d\n", x);
                break;
            }
            x = n * i;
        }
        if(!nya) puts("INSOMNIA");
    }
    return 0;
}
