#include <bits/stdc++.h>
using namespace std;

typedef long long li;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

struct problem {
    // input fields.
    int r, c, ans;
    vector<string> field;
    
    // parse here.
    problem () {
        cin >> r >> c;
        rep(i, r) {
            string row;
            cin >> row;
            field.push_back(row);
        }
    }

    bool within(int x, int y) {
        return x >= 0 && y >= 0 && x < r && y < c;
    }

    // called exactly once. set ans here.
    void solve () {
        int dx[4] = {-1, 0, 1, 0};
        int dy[4] = {0, 1, 0, -1};
        string dcs = "^>v<";

        ans = 0;
        rep(x, r) rep(y, c) {
            if (field[x][y] != '.') {
                int curd = -1;
                rep(d, 4) {
                    if (field[x][y] == dcs[d]) {
                        curd = d;
                        break;
                    }
                }
                
                bool anyok = false;
                bool curok = false;
                rep(d, 4) {
                    int nx = x + dx[d], ny = y + dy[d];
                    while (within(nx, ny)) {
                        bool okcell = field[nx][ny] != '.';
                        anyok |= okcell;
                        curok |= d == curd && okcell;
                        nx += dx[d];
                        ny += dy[d];
                    }
                }
                if (not anyok) {
                    ans = -1;
                    return;
                } if (not curok) {
                    ans += 1;
                }
            }
        }

        return;
    }
};

// generally you don't have to modify below.
int main () {
    int t;
    cin >> t;
    vector<problem> inputs;
    rep (i, t) {
        inputs.push_back(problem());
    }
    #pragma omp parallel for
    rep (i, t) {
        inputs[i].solve();
    }
    rep (i, t) {
        cout << "Case #" << i + 1 << ": ";
        if (inputs[i].ans < 0) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << inputs[i].ans << endl;
        }
    }
    return 0;
}
