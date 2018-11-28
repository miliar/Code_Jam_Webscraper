#include <bits/stdc++.h>

using namespace std;

int r, p, s, nn, n;
char who[300][300];
void solve(int test_id) {
    who['R']['S'] = who['S']['R'] = 'R';
    who['R']['P'] = who['P']['R'] = 'P';
    who['P']['S'] = who['S']['P'] = 'S';

    cout << "Case #" << test_id << ": ";

    cin >> nn >> r >> p >> s;
    n = (1 << nn);
    vector<char> perm;
    for (int i = 0; i < r; i++) {
        perm.push_back('R');
    }
    for (int i = 0; i < p; i++) {
        perm.push_back('P');
    }
    for (int i = 0; i < s; i++) {
        perm.push_back('S');
    }
    sort(perm.begin(), perm.end() );

    vector<char> best;
    best.push_back('Z');

    do {
        bool ok = true;
        vector<char> have = perm, to;
        for (int it = 0; it < nn && ok; it++) {
            to.clear();
            for (int i = 0; i < have.size(); i += 2) {
                if (have[i] == have[i + 1]) {
                    ok = false;
                    break;
                }
                to.push_back( who[ have[i] ][ have[i + 1] ] );
            }
            have = to;
        }
        if (ok) {
            best = min(best, perm);
        }
    }
    while (next_permutation( perm.begin(), perm.end() ) );
    if (best[0] == 'Z') {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        for (int i = 0; i < best.size(); i++) {
            cout << best[i];
        }
        cout << endl;
    }
}

int main () {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
