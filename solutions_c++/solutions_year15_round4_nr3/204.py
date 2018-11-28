#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

const int maxn = 200 + 10;
bool m1[2000], m2[2000];
map<string, int> id;
vector<string> sentence[maxn];
vector<int> wid[maxn];
int n, cnt;

void input() {
    string tmp, word;
    cin >> n;
    cnt = 0; id.clear();
    getline(cin, tmp);
    for (int i = 1; i <= n; ++i) {
        getline(cin, tmp);
        istringstream getword(tmp);
        sentence[i].clear(); wid[i].clear();
        while (getword >> word) {
            if (id.find(word) == id.end())
                id[word] = ++cnt;
            sentence[i].push_back(word);
            wid[i].push_back(id[word]);
        }
    }
}

void solve() {
    int ans = cnt;
    int limit = (1 << (n - 2));
    for (int state = 0; state < limit; ++state) {
        memset(m1, 0, sizeof(m1));
        memset(m2, 0, sizeof(m2));
        for (size_t i = 0; i < wid[1].size(); ++i)
            m1[wid[1][i]] = true;
        for (size_t i = 0; i < wid[2].size(); ++i)
            m2[wid[2][i]] = true;
        for (int i = 3; i <= n; ++i) {
            if ((state >> (i - 3)) & 1) {
                for (size_t j = 0; j < wid[i].size(); ++j)
                    m2[wid[i][j]] = true;
            } else {
                for (size_t j = 0; j < wid[i].size(); ++j)
                    m1[wid[i][j]] = true;
            }
        }
        int tot = 0;
        for (int i = 1; i <= cnt; ++i)
            if (m1[i] && m2[i])
                ++tot;
        ans = min(ans, tot);
    }
    cout << ans << endl;
}

int main() {
    int tt, cas = 0;
    ios::sync_with_stdio(false);
    cin >> tt;
    while (tt--) {
        input();
        cout << "Case #" << (++cas) << ": ";
        solve();
    }
}
