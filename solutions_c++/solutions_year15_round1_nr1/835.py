#include<bits/stdc++.h>
#define sc scanf
#define pr printf
#define fr first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
const int MN = 5010;
const int INF = (1LL<<32) - 1LL;
const int MOD = (1e+9) + 7;
int main(){
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int k = 0, t, n, a[MN];
    for (sc("%d", &t); t--; ) {
        k++;
        sc("%d", &n);
        for (int i = 0; i < n; i++) {
            sc("%d", &a[i]);
        }
        int mx = 0, ans = 0, ans1 = 0;
        for (int i = 1; i < n; i++) {
            mx = max(mx, a[i - 1] - a[i]);
            ans += max(0, a[i - 1] - a[i]);
        }
        for (int i = 0; i < n - 1; i++) {
            ans1 += min(mx, a[i]);
        }
        pr("Case #%d: %d %d\n", k, ans, ans1);
    }
    return 0;
}

