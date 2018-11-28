#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <bitset>
#include <queue>
using namespace std;

#define rep(i, s, t) for (int i = (s); i <= (t); ++i)
#define REP(i, n) rep(i, 1, n)

int n, X, a[111111], ans, r;

void Fate(int ca){
    scanf("%d%d", &n, &X);
    REP(i, n) scanf("%d", &a[i]);
    sort(a + 1, a + 1 + n);
    //reverse(a + 1, a + 1 + n);
    r = n;
    ans = n;
    for (int i = 1; i < r; ++i){
        while (i < r && a[i] + a[r] > X)
            --r;
        if (i < r) ans--;
        r--;
    }
    printf("Case #%d: ", ca);
    printf("%d\n", ans);
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int Ti;
    scanf("%d", &Ti);
    REP(x, Ti){
        Fate(x);
    }
}
/*
4
7 76
30 65 65 19 46 43 52
*/
