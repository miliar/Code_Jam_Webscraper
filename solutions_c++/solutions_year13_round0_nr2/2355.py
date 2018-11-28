#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

bool check(int y0, int x0, int dy, int dx, int n, int m, int el,
           vector <vector <int> > const & ar, vector<bool> const & rows, vector<bool> const & cols) {
    for (int i = y0, j = x0; (i < n) && (j < m); i += dy, j += dx) {
        if (rows[i] || cols[j]) {
            continue;
        }
        if (ar[i][j] != el) {
            return false;
        }
    }
    return true;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        int n, m;
        cin >> n >> m;
        vector <vector <int> > ar(n, vector<int>(m, 0));
        set<int> heights;
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                cin >> ar[j][k];
                heights.insert(ar[j][k]);
            }
        }

        vector <bool> rows(n, false);
        vector <bool> cols(m, false);

        bool no = false;
        for (set<int>::const_iterator it = heights.begin(); it != heights.end(); ++it) {
            int x = *it;
            bool was = false;
            for (int j = 0; j < n; ++j) {
                if (check(j, 0, 0, 1, n, m, x, ar, rows, cols)) {
                    was = true;
                    rows[j] = true;
                }
            }
            for (int j = 0; j < m; ++j) {
                if (check(0, j, 1, 0, n, m, x, ar, rows, cols)) {
                    was = true;
                    cols[j] = true;
                }
            }
            if (!was) {
                no = true;
                break;
            }
        }

        bool temp = true;
        for (vector<bool>::const_iterator it = rows.begin(); it != rows.end(); ++it) {
            temp &= *it;
        }
        for (vector<bool>::const_iterator it = cols.begin(); it != cols.end(); ++it) {
            temp &= *it;
        }
        no |= !temp;

        if (no) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
        }
    }
}
