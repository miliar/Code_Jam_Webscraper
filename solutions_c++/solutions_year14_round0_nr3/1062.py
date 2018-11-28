#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

template< class T >
vector< vector< T > > transpose(vector< vector< T > > a) {
    if (a.empty()) {
        return a;
    }
    int n = a.front().size();
    int m = a.size();
    vector< vector< T > > res(n, vector< T >(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            res[i][j] = a[j][i];
        }
    }
    return res;
}

vector< vector< char > > solve2(int h, int w, int mines) {
    int need_empties = h * w - mines;
    vector< vector< char > > res(h, vector< char >(w, '*'));
    res[0][0] = 'c';
    if (need_empties == 1) {
        return res;
    }
    if (h == 1 || (need_empties == 2 && w != 1)) {
        res.clear();
        return res;
    }
    res[1][0] = '.';
    int empties = 2;
    for (int j = 1; empties + 2 <= need_empties && j < w; ++j) {
        res[0][j] = '.';
        res[1][j] = '.';
        empties += 2;
    }
    if (w == 2 && empties != need_empties) {
        res.clear();
        return res;
    }
    for (int i = 2; empties < need_empties && i < h; ++i) {
        for (int j = 0; empties < need_empties && j < w; ++j) {
            res[i][j] = '.';
            empties += 1;
            if (j == 0 && w != 1 && empties == need_empties) {
                if (i == 2) {
                    empties = need_empties + 1;
                }
                else {
                    swap(res[i][j + 1], res[i - 1][w - 1]);
                }
            }
        }
    }
    if (empties != need_empties) {
        res.clear();
    }
    return res;
}


vector< vector< char > > solve3(int h, int w, int mines) {
    int need_empties = h * w - mines;
    vector< vector< char > > res(h, vector< char >(w, '*'));
    if (need_empties < 6 || need_empties > 3 * w || h < 3 || w == 1) {
        res.clear();
        return res;
    }
    for (int j = 0; j < 2; ++j) {
        for (int i = 0; i < 3; ++i) {
            res[i][j] = '.';
        }
    }
    res[1][0] = 'c';
    int empties = 6;
    for (int j = 2; empties + 2 <= need_empties && j < w; ++j) {
        for (int i = 0; empties < need_empties && i < 3; ++i) {
            res[i][j] = '.';
            empties += 1;
        }
    }
    if (empties != need_empties) {
        res.clear();
    }
    return res;
}

int main() {
    cout.setf(ios_base::fixed);
    cout.precision(7);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ":\n";
        int r, c, m;
        cin >> r >> c >> m;
        auto ans = solve2(r, c, m);
        if (ans.empty()) {
            ans = transpose(solve2(c, r, m));
        }
        if (ans.empty()) {
            ans = solve3(r, c, m);
        }
        if (ans.empty()) {
            ans = transpose(solve3(c, r, m));
        }
        if (ans.empty()) {
            cout << "Impossible\n";
        }
        else {
            for (auto row : ans) {
                for (auto c : row) {
                    cout << c;
                }
                cout << "\n";
            }
        }
    }
    return 0;
}
