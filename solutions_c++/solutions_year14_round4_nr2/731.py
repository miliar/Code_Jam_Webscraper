#include <bits/stdc++.h>
using namespace std;

int n, a[1111];

int res;

void solve(){
    scanf("%d", &n);
    //printf("%d\n", n);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    res = 0;
    int L = 1, R = n;
    while (L <= R){
        int nmin = L;
        for (int i = L; i <= R; i++) if (a[i] < a[nmin]) nmin = i;
        //printf(" %d, %d = %d(%d)\n", L, R, res, nmin);
        if (nmin - L < R - nmin){
            res += nmin - L;
            for (int i = nmin; i >= L + 1; i--) swap(a[i], a[i-1]);
            L++;
        }
        else{
            res += R - nmin;
            for (int i = nmin; i <= R + 1; i++) swap(a[i], a[i+1]);
            R--;
        }
    }
    printf("%d\n", res);
}

int main(){
    freopen("B.inp", "r", stdin);
    //freopen("B2.inp", "w", stdout);
    freopen("B.out", "w", stdout);
    int t; scanf("%d", &t);
    //printf("%d\n", t);
    for (int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
