#pragma COMMENT(linker, "/STACK:64000000");

#include <cstring>
#include <iostream>
#include <iomanip>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int a[212345];
int n;

const int MX = 1000000000;

int dp[11111][11111];

int dfs(int x, int q) {
    if (dp[x][q]) return dp[x][q];
    if (x <= q) return 0;
    int res = MX;
    for(int i = 1; i < x; i++)
        res = min(res, 1 + dfs(i, q) + dfs(x-i, q));
    dp[x][q] = res;
    return res;
}

int get(int q) {
    int res = 0;
    for(int i = 0; i < n; i++)
        if (a[i] > q)
            res += dfs(a[i], q);
    return res;
}

void solve() {
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> a[i];

    int ans = MX;

    for(int i = 1; i <= 1000; i++) {
        ans = min(ans, get(i) + i);
    }

    cout << ans;
}

int main() {
//#ifndef LOCAL
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
//#endif

    ios::sync_with_stdio(false);

    int t;
    cin >> t;



    for(int T = 1; T <= t; T++) {
        cout << "Case #" << T << ": "; solve(); cout << endl;
    }


    return 0;
}