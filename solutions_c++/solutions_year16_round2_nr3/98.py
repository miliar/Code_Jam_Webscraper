#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

bool kuhn(int x, vector<int>& was, const vector<vector<int> >& g, vector<int>& pr) {
    if (was[x]) {
        return false;
    }
    was[x] = true;
    for (int i = 0; i < g[x].size(); ++i) {
        int y = g[x][i];
        if (pr[y] == -1 || kuhn(pr[y], was, g, pr)) {
            pr[y] = x;
            return true;
        }
    }
    return false;
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);

    int T;
    cin >> T;    
    for (int test = 1; test <= T; ++test) {
        int n;
        cin >> n;

        vector<vector<int> > g;
        g.reserve(n);
        unordered_map<string, int> w1s, w2s;
        vector< pair<int, int> > words;
        for (int j = 0; j < n; ++j) {
            string w1, w2;
            int w1x, w2x;
            cin >> w1 >> w2;

            if (w1s.count(w1)) {
                w1x = w1s[w1];
            } else {
                w1x = w1s.size();
                w1s[w1] = w1x;
            }

            if (w2s.count(w2)) {
                w2x = w2s[w2];
            } else {
                w2x = w2s.size();
                w2s[w2] = w2x;
            }

            if (w1x >= g.size()) {
                g.resize(w1x + 1);
            }
            g[w1x].push_back(w2x);
        }

        vector<int> pr(w2s.size(), -1);
        int cnt = 0;
        for (int i = 0; i < w1s.size(); ++i) {
            vector<int> was(w1s.size(), false);
            if (kuhn(i, was, g, pr)) {
                ++cnt;
            }
        }

        cout << "Case #" << test << ": " << n - ((int)w1s.size() + (int)w2s.size() - cnt) << endl;
    }
    cerr << clock() << endl;

    return 0;
}
