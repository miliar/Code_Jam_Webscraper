#include <bits/stdc++.h>

using namespace std;

const int N = 30;

int can[N][N], new_can[N][N];
int n;

bool check(int can[N][N]) {
    vector<int> ord(n);
    for (int i = 0; i < n; ++i) ord[i] = i;
    do {
        vector<int> vis(1, 0);
        for (int i = 0; i < n; ++i) {
            set<int> new_vis;
            for (int mask : vis) {
                bool find = false;
                for (int j = 0; j < n; ++j) {
                    if (can[ord[i]][j] && !(mask >> j & 1)) {
                        new_vis.insert(mask | (1 << j));
                        find = true;
                    }
                }
                if (!find) {
                    return false;
                }
            }
            vis = vector<int>(new_vis.begin(), new_vis.end());
        }
    } while (next_permutation(ord.begin(), ord.end()));
    return true;
}

void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        char buf[N];
        cin >> buf;
        for (int j = 0; j < n; ++j) {
            can[i][j] = buf[j] - '0';
        }
    }
    int ans = 1 << 30;
    for (int mask = 0; mask < 1 << n * n; ++mask) {
        bool ok = true;
        int pos = 0;
        int cost = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                new_can[i][j] = mask >> pos & 1;
                pos++;
                if (new_can[i][j] < can[i][j]) {
                    ok = false;
                }
                cost += new_can[i][j] - can[i][j];
            }
        }
        if (!ok) {
            continue;
        }
        /*
        cout << mask << endl;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cout << new_can[i][j];
            }
            cout << endl;
        }
        */
        if (check(new_can)) {
            ans = min(ans, cost);
        }
    }
    cout << ans << endl;
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        printf("Case #%d: ", testId);
        solve();
        fflush(stdout);
        fprintf(stderr, "%d = %.15f\n", testId, clock() / (double) CLOCKS_PER_SEC);
    }
}

