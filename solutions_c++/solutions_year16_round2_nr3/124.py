#include <bits/stdc++.h>

using namespace std;

string a[1010], b[1010];
int n;

vector<int> g[1010];
set<string> wa, wb;
map<string, int> mpa, mpb;

int with[1010];
bool was[1010];

bool dfs(int x) {
    if (was[x] == true) {
        return false;
    }
    was[x] = true;
    for (int i = 0; i < g[x].size(); i++) {
        int to = g[x][i];
        if (with[to] == -1 || dfs(with[to]) ) {
            with[to] = x;
            return true;
        }
    }
    return false;
}

void solve(int test_id) {
    memset(with, -1, sizeof(with) );
    wa.clear(); wb.clear();
    mpa.clear(); mpb.clear();
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i];
        wa.insert(a[i]);
        wb.insert(b[i]);
    }
    cout << "Case #" << test_id << ": ";

    int lstA, lstB;

    lstA = 0;
    for (auto it = wa.begin(); it != wa.end(); ++it) {
        mpa[ *it ] = lstA;
        lstA++;
    }

    lstB = 0;
    for (auto it = wb.begin(); it != wb.end(); ++it) {
        mpb[ *it ] = lstB;
        lstB++;
    }

    for (int i = 0; i < 1010; i++) {
        g[i].clear();
    }

    for (int i = 0; i < n; i++) {
        g[ mpa[ a[i] ] ].push_back( mpb[ b[i] ] );
    }
    int res = 0;
    for (int i = 0; i < lstA; i++) {
        memset(was, 0, sizeof(was));
        if ( dfs(i) ) {
            res++;
        }
    }
    res = lstA + lstB - res;
    cout << n - res << endl;
}

int main () {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
