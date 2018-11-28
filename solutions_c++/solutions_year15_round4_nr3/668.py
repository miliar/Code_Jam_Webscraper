#include<iostream>
#include<queue>
#include<string>
#include <cstdio>
#include<vector>
#include<cmath>
#include<ctime>
#include<memory.h>
#include<map>
#include <cmath>
#include<algorithm>
#include<set>
using namespace std;
#define y1 anaasfasf
int all = 0;
int n, m;
string s;
int fr[255];
vector < int > v[205];
int g[5000][5];
map < string, int > mp;
int add(string &s) {
    if (!mp.count(s)) {
        mp[s] = ++all;
    }
    return mp[s] - 1;
}

vector < int > get(string s) {
    vector < int > ret;
    s = s + ' ';
    string cs = "";
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ' ) {
            if (cs.size() > 0) ret.push_back(add(cs));
            cs = "";
        }
        else cs = cs + s[i];
    }
    return ret;
}
bool bit(int mask, int x) {
    mask &= ( 1 << x );
    return mask > 0;
}
void solve() {
    mp.clear(); all = 0;
    cin >> n;
    getline(cin, s);
    for (int i = 0; i < n; ++i) {
       getline(cin, s);
       v[i] = get(s);

    }
    int ans = all;
    fr[0] = 0, fr[1] = 1;
    for (int i = 0; i < all; ++i)
        for (int j = 0; j < 2; ++j)
            g[i][j] = 0;
    for (int i = 0; i < v[0].size(); ++i)
        g[v[0][i]][0]++;
    for (int i = 0; i < v[1].size(); ++i)
        g[v[1][i]][1]++;
    for (int i = 0; i < (1 << n); ++i) {
        if (bit(i, 0) || !bit(i, 1)) continue;
        for (int j = 2; j < n; ++j) {
            fr[j] = bit(i, j);
        }
        for (int j = 2; j < n; ++j) {
            for (auto u : v[j]) {
                g[u][fr[j]]++;
            }
        }
        int ret = 0;
        for (int j = 0; j < all; ++j) {
            if (g[j][0] && g[j][1]) ret++;
        }
        for (int j = 2; j < n; ++j)
            for (auto u : v[j])
                g[u][fr[j]]--;
        ans = min(ans, ret);
    }
    cout << ans << endl;
}
int main() {
    #ifdef FurkoHome
        freopen("input.txt","r",stdin);
    //    freopen("A-large.in","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    ios::sync_with_stdio(false);
    int T; cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}
