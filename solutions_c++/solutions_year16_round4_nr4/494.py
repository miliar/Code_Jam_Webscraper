#include <bits/stdc++.h>

using namespace std;

int n;
string can[30];
bool busy[50];
bool rec(int t, const vector<int> &perm) {
    if (t == n) {
        return true;
    }
    int oc = 0;
    for (int i = 0; i < n; i++) {
        if (busy[i] == true) {
            continue;
        }
        int w = perm[t];
        if (can[w][i] == '0') {
            continue;
        }
        oc++;
        busy[i] = true;
        bool res = rec(t + 1, perm);
        busy[i] = false;
        if (res == false) {
            return false;
        }
    }
    if (oc == 0) {
        return false;
    }
    return true;
}

bool check() {
    vector<int> perm;
    for (int i = 0; i < n; i++) {
        perm.push_back(i);
    }

    bool ok = true;
    do {
        if ( rec(0, perm) == false ) {
            ok = false;
            break;
        }
    }
    while ( next_permutation(perm.begin(), perm.end() ) );

    return ok;
}

void solve(int test_id) {
    cout << "Case #" << test_id << ": ";
    cin >> n;
    vector<pair<int, int> > all;
    for (int i = 0; i < n; i++) {
        cin >> can[i];
        for (int j = 0; j < n; j++) {
            if (can[i][j] == '0') {
                all.push_back( make_pair(i, j) );
            }
        }
    }
    int ans = 1E9;
    for (int i = 0; i < (1 << all.size()); i++) {
        for (int j = 0; j < all.size(); j++) {
            if ( i & (1 << j) ) {
                can[ all[j].first ][ all[j].second ] = '1';
            }
        }
        if ( check() ) {
            ans = min(ans, __builtin_popcount(i) );
        }
        for (int j = 0; j < all.size(); j++) {
            if ( i & (1 << j) ) {
                can[ all[j].first ][ all[j].second ] = '0';
            }
        }
    }
    cout << ans << endl;
}

int main () {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
