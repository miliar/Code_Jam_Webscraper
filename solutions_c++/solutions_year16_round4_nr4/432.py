#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;

long double a[maxn];

int n;

string s[5];
string b[5];

bool ok() {
    int p[n];
    for (int i= 0; i < n; i++)
        p[i] = i;
    int ma = (1 << n);
    bool used[ma];
    bool nex[ma];
    do {
        for (int i = 0; i < ma; i++)
            used[i] = 0;
        used[0] = true;
        for (int i = 0; i < n; i++) {
            int now = p[i];
            for (int j = 0; j < ma; j++) {
                nex[j] = false;
            }
            for (int j = 0; j < ma; j++) {
                if (used[j]) {
                    int mask = j;
                    int cnt = 0;
                    for (int k = 0; k < n; k++) {
                        if (b[now][k] == '1' && ((mask & (1 << k)) == 0)) {
                            cnt++;
                            nex[mask ^ (1 << k)] = true;
                        }
                    }
                    if (cnt == 0)
                        return false;
                }
            }
            for (int i = 0; i < ma; i++)
                used[i] = nex[i];
        }
    } while (next_permutation(p, p + n));
    return true;
}
void solve() {

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
        b[i] = s[i];
    }
    vector < pair < int, int > > a;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (s[i][j] == '0')
                a.push_back({i, j});
        }
    int u = a.size();
    int ans = u;
    for (int mask = 0; mask < (1 << u); mask++) {

        int tmp = 0;

        for (int j = 0; j < u; j++) {
            if (mask & (1 << j)) {
                tmp++;
                b[a[j].first][a[j].second] = '1';
            }
        }

        if (ok()) {
            ans = min(ans, tmp);
        }

        for (int j = 0; j < u; j++) {
            if (mask & (1 << j)) {
                b[a[j].first][a[j].second] = '0';
            }
        }
    }
    cout << ans << endl;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test;
    cin >> test;
    for (int id = 1; id <= test; id++) {
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}