#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

template < typename T > T next() { T tmp; cin >> tmp; return tmp; }

bool in(int x, int a, int b) {
    return a <= x && x < b;
}

void solve() {
    int r = next< int >();
    int c = next< int >();
    vector< string > f(r, "");
    generate(f.begin(), f.end(), next< string >);
    

    int d[256];
    d['<'] = 0;
    d['^'] = 1;
    d['>'] = 2;
    d['v'] = 3;

    int ds[4][2] = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };
    int ans = 0;

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (f[i][j] == '.') continue;
            for (int k = 1; k < r + c; ++k) {
                int px = i + k * ds[ d[f[i][j]] ][0];
                int py = j + k * ds[ d[f[i][j]] ][1];
                if (in(px, 0, r) && in(py, 0, c)) {
                    if (f[px][py] != '.') {
                        break;
                    }
                } else {
                    ans += 1;
                    break;
                }

            }
        }
    }
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (f[i][j] == '.') continue;
            int b = 0;
            for (int dir = 0; dir < 4; ++dir) {
                for (int k = 1; k < r + c; ++k) {
                    int px = i + k * ds[ dir ][0];
                    int py = j + k * ds[ dir ][1];
                    if (in(px, 0, r) && in(py, 0, c)) {
                        if (f[px][py] != '.') {
                            break;
                        }
                    } else {
                        b += 1;
                        break;
                    }
                }
            }
            if (b == 4) {
                cout << "IMPOSSIBLE\n";
                return;
            }
        }
    }
    cout << ans << "\n";

}

int main() {
    int t = next< int >();
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
