#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int c2d(char c) {
    if (c == '.') return 0;
    if (c == '^') return 1;
    if (c == '>') return 2;
    if (c == 'v') return 3;
    if (c == '<') return 4;
    return -1;
}

int solve() {
    int r, c;
    cin >> r >> c;
    vector< vector< int > > field(r, vector< int >(c));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            do {
                field[i][j] = c2d(getchar());
            } while (field[i][j] == -1);
        }
    }
    vector< int > ftir(max(r, c), max(r, c));
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (field[i][j] != 0) {
                ftir[i] = j;
                // cerr << "ftir " << i << " = " << j << endl;
                break;
            }
        }
    }
    vector< int > ltir(max(r, c), -1);
    for (int i = 0; i < r; ++i) {
        for (int j = c - 1; j >= 0; --j) {
            if (field[i][j] != 0) {
                ltir[i] = j;
                // cerr << "ltir " << i << " = " << j << endl;
                break;
            }
        }
    }
    vector< int > ftic(max(r, c), max(r, c));
    for (int j = 0; j < c; ++j) {
        for (int i = 0; i < r; ++i) {
            if (field[i][j] != 0) {
                ftic[j] = i;
                // cerr << "ftic " << j << " = " << i << endl;
                break;
            }
        }
    }
    vector< int > ltic(max(r, c), -1);
    for (int j = 0; j < c; ++j) {
        for (int i = r - 1; i >= 0; --i) {
            if (field[i][j] != 0) {
                ltic[j] = i;
                // cerr << "ltic " << j << " = " << i << endl;
                break;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            auto& x = field[i][j];
            if (x != 0) {
                if (ftir[i] >= j && ftic[j] >= i && ltir[i] <= j && ltic[j] <= i) {
                    // cerr << "quit " << i << " " << j << endl;
                    return -1;
                }
                if (((x == 1) && (ftic[j] == i)) ||
                    ((x == 2) && (ltir[i] == j)) ||
                    ((x == 3) && (ltic[j] == i)) ||
                    ((x == 4) && (ftir[i] == j))) {
                    ans += 1;
                }
            }
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        auto ans = solve();
        cout << "Case #" << t << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE";
        }
        else {
            cout << ans;
        }
        cout << "\n";
    }
    return 0;
}
