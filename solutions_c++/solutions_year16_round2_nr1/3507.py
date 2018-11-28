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
string nums[] = {"ZERO", "ONE", "TWO",   "THREE", "FOUR",
                 "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
bool ok(int i, map<char, int> cnt) {
    map<char, int> mp;
    rep(j, nums[i].size()) mp[nums[i][j]]++;
    bool f = true;
    for (auto &e : mp) {
        f &= e.second <= cnt[e.first];
    }
    return f;
}
string ans;
void dfs(int i, map<char, int> cnt, string s) {
    if(i==10) return;
    if (ans != "") return;
    bool f = true;
    for (auto e : cnt) f &= e.second == 0;
    if (f) {
        ans = s;
        return;
    }
    if (ok(i, cnt)) {
        auto tmp=cnt;
        rep(j, nums[i].size()) tmp[nums[i][j]]--;
        dfs(i, tmp, s + string(1, i + '0'));
    }
        dfs(i + 1, cnt, s);
}

string solve() {
    ans = "";
    string s;
    cin >> s;
    cerr << s << endl;
    map<char, int> cnt;
    rep(i, s.size()) cnt[s[i]]++;
    dfs(0, cnt, "");
    cerr << ans << endl;
    for (auto e : cnt) {
        cerr << e.first << ", " << e.second << endl;
    }

    return ans;
}
int main() {
    int T;
    cin >> T;
    rep(i, T) { cout << "Case #" << i + 1 << ": " << solve() << endl; }
    return 0;
}
