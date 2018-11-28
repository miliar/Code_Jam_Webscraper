#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>

using namespace std;
typedef long long li;
typedef pair <li, li> pi;
#define rep(i, n) for(int i = 0; i < (int)(n); ++i)

void solve() {
    int n;
    cin >> n;
    int init = 0;
    auto pos = [&](int i, int j) {
        return i * n + j;
    };
    auto posbit = [&](int i, int j) {
        return 1 << pos(i, j);
    };

    rep(i, n) {
        string k;
        cin >> k;
        rep(j, n) {
            if (k[j] == '1') {
                init |= posbit(i, j);
            }
        }
    }

    int len = n * n;
    int ans = len;
    rep(mask, 1 << len) {
        if ((mask & init) != init) {
            continue;
        }

        bool ok = true;
        vector<int> order;
        rep(i, n) {
            order.push_back(i);
        }
        do {
            function<bool(int, int)> dfs = [&](int ord, int used) {
                if (ord == n) {
                    return true;
                }
                int worker = order[ord];
                int ability = (mask >> (n * worker)) & ((1 << n) - 1);
                int avail = ((1 << n) - 1) ^ used;
                if ((avail & ability) == 0) {
                    return false;
                }
                rep(use, n) {
                    if (ability & avail & (1 << use)) {
                        if (!dfs(ord+1, used | (1 << use))) {
                            return false;
                        }
                    }
                }
                return true;
            };
            if (!dfs(0, 0)) {
                ok = false;
                break;
            }
        } while (next_permutation(order.begin(), order.end()));
        if (ok) {
            ans = min(ans, __builtin_popcount(mask ^ init));
        }
    }
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    rep(i, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
