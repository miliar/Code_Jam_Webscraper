#include<bits/stdc++.h>
#define sc scanf
#define pr printf
#define fr first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
const int MN = 510;
const long long INF = (1LL<<30);
const int MOD = (1e+9) + 7;

bool dp[MN] = {true};
int t, c, d, v, a[MN];

int main(){
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    sc("%d", &t);
    for (int k = 1; k <= t; k++) {
        pr("Case #%d: ", k);
        sc("%d%d%d", &c, &d, &v);
        for (int i = 0; i < d; i++){
            sc("%d", &a[i]);
        }
        a[d++] = v + 1;
        int ans = 0;
        long long res = 1;
        for (int p = 0; p < d; p++) {
            if(res < 1LL * a[p]) {
                res += 1LL * c * res;
                p--;
                ans++;
            }
            else {
                res += 1LL * c * a[p];
            }
            //pr("%lld\n", res);
        }
        pr("%d\n", ans);
    }

    return 0;
}

