#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <stack>
#include <queue>
#include <set>

#define rep(i,n) for(int i=0;i<(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

int trie(vector<string> &str) {
    if (str.size() == 0) return 0;
    vector<string> pre[26];
    int ans = 1;
    rep(i, str.size()) {
        if (str[i].size() == 0) continue;
        pre[str[i][0] - 'A'].push_back(str[i].substr(1));
    }
    rep(i, 26) {
        ans += trie(pre[i]);
    }
    return ans;
}

pair<long long, long long> dp[5][1 << 8];
long long base[1 << 8];

const long long mod = 1000000007;

int M, N;

pair<long long, long long> rec(long long n, int mask) {
    if (mask == 0) return make_pair(-(1LL << 50), 0);
    if (dp[N][mask].first >= 0) return dp[N][mask];
    if (n == 1) return make_pair(base[mask], 1);

    long long ans = -1;
    long long count = 0;
    rep(i, 1 << M) {
        if (i == 0) continue;
        if ((mask | i) != mask) continue;
        pair<long long, long long> res = rec(n - 1, mask ^ i);
        if (ans == res.first + base[i]) {
            count = (count + res.second) % mod;
        } else if (ans < res.first + base[i]) {
            ans = res.first + base[i];
            count = res.second;
        }
    }
    return make_pair(ans, count % mod);
}

void solve() {
    cin >> M >> N;
    vector<string> strs(M);
    
    rep(i, M)cin >> strs[i];

    rep(i, N + 1) {
        rep(j, 1 << M) {
            dp[i][j] = make_pair(-1, 0);
        }
    }

    rep(i, 1 << M) {
        vector<string> sub;
        rep(j, M) {
            if ((i >> j) & 1) sub.push_back(strs[j]);
            base[i] = trie(sub);
        }
    }
    
    pair<long long, long long> ans = rec(N, (1 << M) - 1);
    cout << ans.first << " " << ans.second << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
