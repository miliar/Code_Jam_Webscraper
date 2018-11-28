#include <bits/stdc++.h>
using namespace std;

string runTest() {
    int n, r, p, ns; cin >> n >> r >> p >> ns;
    int two = r + p + ns;
    vector<pair<string, int> > s = {{"P", p}, {"R", r}, {"S", ns}};
    while (two > 1) {
        two /= 2;
        decltype(s) t;
        for (int i = 0; i < 3; ++i) {
            for (int j = i + 1; j < 3; ++j) {
                t.push_back({min(s[i].first + s[j].first, s[j].first + s[i].first), two - s[3 - i - j].second});
            }
        }
        sort(t.begin(), t.end());
        for (auto &x : t) if (x.second < 0) return "IMPOSSIBLE";
        s = t;
    }
    for (auto &x : s) if (x.second == 1) return x.first;
    return "SOMETHING WRONG";
}

int main() {
    ios::sync_with_stdio(false);
    int tc; cin >> tc;
    for (int t = 1; t <= tc; ++t) {
        cout << "Case #" << t << ": " << runTest() << endl;
    }
    return 0;
}
