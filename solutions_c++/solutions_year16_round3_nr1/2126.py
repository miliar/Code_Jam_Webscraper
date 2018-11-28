#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

using namespace std;
using ll = long long;

#define all(c) (c).begin(), (c).end()
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const ll INF = 1e9;
const ll MOD = 1e9 + 7;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int N;
vector<int> P;
void vaild(vector<int> vec, vector<string> ans) {
    int sum = 0;
    for (auto s : ans) {
        rep(i, s.size()) vec[s[i] - 'A']--;
        rep(i, vec.size()) sum += vec[i];
        rep(i, vec.size()) if (vec[i] * 2 > sum) assert(false);
    }
}
string solve() {
    string res = "";
    vector<string> ans;
    cin >> N;
    P = vector<int>(N);
    rep(i, N) cin >> P[i];
    auto t = P;

    int sum = 0;
    rep(i, N) sum += P[i];

    while (sum) {
        int t = max(0, sum - 2) / 2;
        string s;
        rep(i, N) {
            if (P[i] > t && s.size() < 2) {
                s += string(1, i + 'A');
                P[i]--;
                i--;
                if (sum == 3) break;
            }
        }
        rep(i, N) if (P[i] && s.size() < 2) {
            if (sum == 3) break;
            s += string(1, i + 'A');
            P[i]--;
        }
        rep(i, N) if (2 * P[i] > sum) {
            cerr << sum << endl;
            cerr << i << ", " << P[i] << endl;
            assert(false);
        }
        // cerr << "debug: " << sum << ", " << t << ", " << s << endl;
        assert(t != 1 || s.size() <= 2);
        sum -= s.size();
        res += s + " ";
        ans.push_back(s);
    }

    vaild(t, ans);
    res = "";
    rep(i,ans.size()) {
        res += ans[i];
        if(i+1!=ans.size()) res+=" ";
    }

    return res;
}
int main() {
    int t;
    cin >> t;
    rep(i, t) {
        auto ans = solve();
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
