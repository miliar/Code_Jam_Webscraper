#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

bool check(vector<vector<int> >& f, int curc) {
    if (curc < 0) return true;

    int r = f.size();
    int c = f[0].size();

    for (int i = 0; i < r; ++i) {
        if (f[i][curc] == -1) break;
        f[i][curc] = 0;
        for (int dx = max(0, curc - 1); dx <= min(c - 1, curc + 1); ++dx) {
            for (int dy = max(0, i - 1); dy <= min(r - 1, i + 1); ++dy) {
                if (dx == curc && dy == i) continue;
                if (f[dy][dx] == -1) {
                    ++f[i][curc];
                }
            }
        }
    }
    
    bool ok = true;
    for (int i = 0; i < r; ++i) {
        if (f[i][curc] == -1) break;
        bool has = false;
        for (int dx = max(0, curc - 1); dx <= min(c - 1, curc + 1); ++dx) {
            for (int dy = max(0, i - 1); dy <= min(r - 1, i + 1); ++dy) {
                if (f[dy][dx] == 0) {
                    has = true;
                }
            }
        }
        if (!has) ok = false;
    }
    return ok;
}

bool solve(vector<vector<int> >& f, int m, int curc) {
    if (m < 0) return false;

    int r = f.size();
    int c = f[0].size();

    if (m == 0) {
        if (check(f, curc - 1))
            return true;
    }
    if (curc >= c)
        return false;

    for (int i = 0; i < min(m, r); ++i) {
        f[i][curc] = 1;
        if (check(f, curc - 1)) {
            if (solve(f, m - i - 1, curc + 1))
                return true;
        }
    }
    for (int i = 0; i < min(m, r); ++i)
        f[i][curc] = -1;
    return false;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int r, c, m;
        cin >> r >> c >> m;
        vector<vector<int> > f(r, vector<int>(c, -1));
        if (r * c - m == 1) {
            cout << "Case #" << t << ":\n";
            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    if (i == 0 && j == 0) {
                        cout << "c";
                    } else {
                        cout << "*";
                    }
                }
                cout << endl;
            }
            continue;
        }
        bool ok = solve(f, r * c - m, 0);

        cout << "Case #" << t << ":\n";
        if (ok) {
            bool put_c = false;
            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    if (f[i][j] == -1) cout << "*";
                    else if (f[i][j] == 0 && !put_c) {
                        cout << "c";
                        put_c = true;
                    } else {
                        cout << ".";
                    }
                }
                cout << endl;
            }
        } else {
            cout << "Impossible\n";
        }
    }

    return 0;
}