#include <bits/stdc++.h>

using namespace std;

map<string, int> id1;
map<string, int> id2;

vector <pair<int, int> > mp;

int used1[30], used2[30];

const int maxn = 16;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        id1.clear();
        id2.clear();

        mp.resize(0);
        int n;
        cin >> n;
        int cnt1 = 0, cnt2 = 0;

        for (int i = 0; i < n; ++i) {
            string s, t;
            cin >> s >> t;
            int v1 = cnt1, v2 = cnt2;
            if (id1.count(s) > 0) {
                v1 = id1[s];                   
            } else {
                id1[s] = v1;
                ++cnt1;
            }
            if (id2.count(t) > 0) {
                v2 = id2[t];
            } else {
                id2[t] = v2;
                ++cnt2;
            }
            mp.push_back(make_pair(v1, v2));
        }

        int res = n;

        for (int msk = 0; msk < (1 << n); ++msk) {
            for (int i = 0; i < cnt1; ++i) {
                used1[i] = 0;
            }
            for (int i = 0; i < cnt2; ++i) {
                used2[i] = 0;
            }

            int cr = 0;
            for (int i = 0; i < n; ++i) {
                if ((msk >> i) & 1) {
                    ++cr;
                    used1[mp[i].first] = 1;
                    used2[mp[i].second] = 1;
                }
            }
            int fl = 1;
            for (int i = 0; i < cnt1; ++i) {
                if (used1[i] == 0) fl = 0;
            }
            for (int i = 0; i < cnt2; ++i) {
                if (used2[i] == 0) fl = 0;
            }

            if (fl == 1) {
                res = min(res, cr);
            }

        }

        printf("Case #%d: %d\n", test, n - res);
    }

}