#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <utility>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

template <class T>
inline int RD(T &x) {
    x = 0;
    char ch = getchar();
    while(!isdigit(ch)) { ch = getchar();  if(ch == EOF) return 0; }
    while(isdigit(ch)) { x *= 10; x += ch - '0'; ch = getchar(); }
    return 1;
}

template <class T>
void PT(T a) {
     if(a > 9) PT(a / 10);
     putchar(a % 10 + '0');
}

typedef __int64 LL;

bool vis[10];

void findD(LL x) {
    while(x) {
        int tmp = (int)(x % 10);
        vis[tmp] = true;
        x = x / 10;
    }
}

bool check() {
    for(int i = 0; i < 10; i++)
        if(!vis[i])
            return false;
    return true;
}

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    LL n, x;
    int cas = 0, t;
    RD(t);
    bool ans;
    while(t--) {
        cas++;
        printf("Case #%d: ", cas);
        RD(n);
        if(n == 0) {
            puts("INSOMNIA");
            continue;
        }
        ans = false;
        memset(vis, 0, sizeof vis);
        x = n;
        for(int i = 2; i <= 101; i++) {
            findD(x);
            if(check()) {
                ans = true;
                printf("%I64d\n", x);
                break;
            }
            x = n * i;
        }
        if(!ans)
            puts("INSOMNIA");
    }
    return 0;
}
