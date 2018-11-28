#include <bits/stdc++.h>
using namespace std;

int n, x, a[11111];

void solve(){
    scanf("%d%d", &n, &x);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    sort(a, a + n);
    int l = 0, res = 0;
    for (int i = n - 1; i >= l; i--){
        res++;
        if (a[i] + a[l] <= x && i != l) l++;
    }
    printf("%d\n", res);
}

int main(){
    freopen("A.inp", "r", stdin);
    freopen("A.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
