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
string S;

void flip(string &s, int n) {
    rep(i, n) {
        if (s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';
    }
}

int find(string s) {
    char c = s.front();
    int res = -1;
    rep(i, s.size()) {
        if (c != s[i]) {
            res = i;
            break;
        }
    }
    return res;
}

int bfs(string s) {
    set<string> used;
    int ret = INF;
    queue<pair<string, int>> que;
    que.push(make_pair(s, 0));
    while (que.size()) {
        auto p = que.front();
        que.pop();
        auto t = p.first;
        if (count(all(t), '+') == t.size()) return p.second;
        if (used.count(t)) continue;
        used.insert(t);
        auto pos = find(t);
        if (pos != -1) {
            flip(t, pos);
            reverse(t.begin(), t.begin() + pos);
            que.push(make_pair(t, p.second + 1));
            // cerr << "debug: " << p.first << " -> " << t << endl;
        }

        t = p.first;
        flip(t, t.size());
        reverse(all(t));
        que.push(make_pair(t, p.second + 1));
        // cerr << "debug: " << p.first << " -> " << t << endl;
    }
    return ret;
}

void solve() {
    printf("%d\n", bfs(S));
    return;
    string s = S;
    int ans = 0;
    while (1) {
        auto pos = s.find('-');
        if (pos == string::npos) break;
        flip(s, pos + 1);
        reverse(s.begin(), s.begin() + pos);
        ans++;
    }
    printf("%d\n", ans);
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cin >> S;
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}
