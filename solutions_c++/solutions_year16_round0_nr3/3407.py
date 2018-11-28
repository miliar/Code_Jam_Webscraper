#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int n, m;
int wei[100];
long long int son[100];

bool get_son(long long a,int b) {
    long long i = 2;
    for(; i*i <= a; ++i) {
        if(a % i == 0) {
            son[b] = i;
            return true;
        }
    }
    return false;
}

long long int getnum(int len, int i) {
    long long ans = 0;
    for(int t = len-1; t >=0; --t) {
        ans *= (long long int)i;
        ans += wei[t];
    }
    return ans;
}

bool check(long long t, int n) {
    int len = 0;
    wei[len++] = 1;
    while(t) {
        if(t & 1) wei[len++] = 1;
        else wei[len++] = 0;
        t >>= 1;
    }
    while(len < n-1) wei[len ++] = 0;
    wei[len ++] = 1;
    wei[len] = 0;
    long long a, b, c;
    //0 - len-1
    for(int i = 2; i <= 10; ++i) {
        a = getnum(len, i);
        if(!get_son(a, i)) {
            return false;
        }
    }
    return true;
}

void do_print(long long t, int n) {
    int len = n;
    for(int i=len-1; i >= 0; --i) {
        printf("%d", wei[i]);
    }
    for(int j = 2; j <= 10; ++j) {
        printf(" %lld", son[j]);
    }
    puts("");
}

void solve(int n, int m) {
    int count = 0;
    long long int t = 0;
//    printf("%lu\n", t);
    while(1) {
        if(check(t, n)) {
            count ++;
            do_print(t, n);
            if(count == m) return ;
        }
        t ++;
    }
}

int main() {
    freopen("C-small-attempt0.in", "r",stdin);
    freopen("out", "w",stdout);
    int T;
    scanf("%d",&T);
    int pos = 1;
    while(T--) {
        scanf("%d %d", &n, &m);
        printf("Case #%d:\n", pos++);
        solve(n, m);
    }

    return 0;
}