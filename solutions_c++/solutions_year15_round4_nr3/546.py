#include <bits/stdc++.h>
using namespace std;

map<string, int> mp;

vector<int> readLine() {
    string s;
    getline(cin, s);
    stringstream sin (s);
    vector<int> result;
    for (string t; sin >> t; ) {
        if (mp.count(t) == 0) mp.emplace(t, mp.size());
        result.push_back(mp[t]);
    }
    return result;
}

int cnt = 0;

int solve() {
    cerr << "SOLVING " << ++cnt << endl;
    mp.clear();
    int n; assert(cin >> n >> ws);
    vector<vector<int> > words (n);
    for (int i = 0; i < n; ++i) {
        words[i] = readLine();
    }
    int result = 1e9;
    for (int mask = 1; mask < 1 << n; mask += 4) {
        vector<bool> a[2];
        a[0].resize(mp.size());
        a[1].resize(mp.size());
        for (int i = 0; i < n; ++i) {
            vector<bool> &foo = a[mask >> i & 1];
            for (auto x : words[i]) foo[x] = true;
        }
        int foo = 0;
        for (int i = 0; i < (int) mp.size(); ++i) if (a[0][i] && a[1][i]) ++foo;
        result = min(result, foo);
    }
    return result;
}

int main() {
    assert(freopen("C.in", "r", stdin));
    assert(freopen("C.out", "w", stdout));
    ios::sync_with_stdio(false);
    int numTests; cin >> numTests;
    for (int test = 0; test < numTests; ++test) {
        cout << "Case #" << test + 1 << ": " << solve() << '\n';
    }
    return 0;
}
