#include <cstdio>
#include <algorithm>
using namespace std;

int solve() {
    int n, x;
    scanf("%d %d", &n, &x);
    int s[n];
    for(int i = 0; i < n; i ++)
        scanf("%d", &s[i]);
    sort(s, s + n);
    int l, r;
    int pud = 0;
    for(l = 0, r = n-1; l < r; l ++, r --, pud ++) {
        while(l < r && s[l] + s[r] > x) {
            r --;
            pud ++;
        }
    }
    if(l == r)
        pud ++;
    return pud;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++)
        printf("Case #%d: %d\n", i, solve());
}