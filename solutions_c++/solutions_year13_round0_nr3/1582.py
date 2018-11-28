#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int n = 10000000;

LL pal[100];
int tot;
int a[14];

bool ispal(LL x ) {
     int len = 0;
     while (x) {
           a[len++] = x % 10;
           x /= 10;
     }
     for (int i = 0; i < (len>>1); ++i )
         if (a[i] != a[len-1-i]) return false;
     return true;
}

void prepare() {
     tot = 0;
     for (int i = 1; i <= n; i++ )
         if (ispal(i) && ispal((LL)i*i)) pal[tot++] = (LL)i*i;
}

int count(LL x ) {
    for (int i = 0; i < tot; i++ )
        if (pal[i] > x) return i;
    return tot;
}

void work() {
     int cas;
     LL A, B;
     scanf("%d",&cas);
     for (int run = 1; run <= cas; run++ ) {
         cin >> A >> B;
         printf("Case #%d: %d\n",run,count(B)-count(A-1));
     }
}

int main() {
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    prepare();
    work();
    return 0;
}
