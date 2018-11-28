#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#define MOD 1000002013
using namespace std;

struct node {
    long long o, e, p;
}a[1010];

bool cmp(const node x, const node y) {
    if (x.o < y.o) return true;
    if (x.o == y.o && x.e < y.e) return true;
    return false;
}

int main() {
    freopen("/Users/L/Downloads/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/L/Downloads/ans.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int kase = 1; kase <= T; kase++) {
        int n, m;
        scanf("%d%d", &n, &m);
        
        long long ans = 0;
        for (int i = 0; i < m; i++) {
            scanf("%lld%lld%lld", &a[i].o, &a[i].e, &a[i].p);
            long long k = a[i].e - a[i].o;
            ans = (ans + (2*n-k+1)*k/2 % MOD *a[i].p) % MOD;
        }
        sort(a, a+m, cmp);
        a[m].o = 1000000010;
        
        for (int i = 0; i < m; i++) {
            while (a[i].p > 0) {
                int j = i;
                while (j < m && (a[j+1].o <= a[i].e || a[j].p == 0)) j++;
                
                if (j == m || a[i].e >= a[j].e) {
                    if (j != m) {
                        ans = (ans - (2*n-(a[i].e-a[i].o-1))*(a[i].e-a[i].o)/2 % MOD * a[i].p + MOD) % MOD;
                    }
                    a[i].p = 0;
                }
                else if (a[i].p > a[j].p) {
                    ans = (ans - (2*n-(a[j].e-a[i].o-1))*(a[j].e-a[i].o)/2 % MOD * a[j].p + MOD) % MOD;
                    a[i].p -= a[j].p;
                    a[j].e = a[i].e;
                }
                else {
                    ans = (ans - (2*n-(a[j].e-a[i].o-1))*(a[j].e-a[i].o)/2 % MOD * a[i].p + MOD) % MOD;
                    a[j].p -= a[i].p;
                    a[i].p = 0;
                }
            }
        }
        
        while (ans < 0) ans += MOD;
        printf("Case #%d: %lld\n", kase, ans % MOD);
    }
    return 0;
}