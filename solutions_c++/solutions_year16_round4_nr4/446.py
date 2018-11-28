#include <bits/stdc++.h>

using namespace std;

bool operates[5][5];
bool can[5][5];
bool in_use[5];
int n;
vector <int> v;

bool test (int i) {
    if (i == n) return true;
    bool found = false;
    for (int j = 0; j < n; ++j) {
        if (!in_use[j] and can[v[i]][j]) {
            found = true;
            in_use[j] = true;
            if (!test (i + 1)) return false;
            in_use[j] = false;
        }
    }
    return found;
}

int main (void) {

    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        cin >> n;
        memset (operates, 0, sizeof operates);
        for (int i = 0; i < n; ++i) {
            string s; 
            cin >> s;
            for (int j = 0; j < s.size(); ++j) {
                if (s[j] == '1') operates[i][j] = true;
            }   
        }
        int ans = n*n;
        for (int mask = 0; mask < (1<<(n*n)); ++mask) {
            memset (can, 0, sizeof can);
            int cost = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (!operates[i][j] and ((mask>>(i*n+j))&1)) cost++;
                    can[i][j] = ((mask>>(i*n+j))&1) or operates[i][j];
                }
            }
            v.clear();
            bool good = true;
            for (int i = 0; i < n; ++i) v.push_back (i);
            do {
                memset (in_use, 0, sizeof in_use);
                if (!test(0)) good = false;
            } while (good and next_permutation (v.begin(), v.end()));
           // for (int i = 0; i < n; ++i, cout << endl) 
           //     for (int j = 0; j < n; ++j) cout << can[i][j];
           // cout << good << " - " << cost << " === " << endl;
            if (good) ans = min (ans, cost);
        }
        printf ("Case #%d: %d\n", c, ans);
    }
}
