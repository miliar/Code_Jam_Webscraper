#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
using namespace std;


bool rowHas (vector<vector<int> > v, int start, int end, int row, int num) {
    for (int i = start; i != end; ++i) {
        if (v[row][i] > num) {
            return true;
        }
    }
    return false;
}

bool colHas (vector<vector<int> > v, int start, int end, int col, int num) {
    for (int i = start; i != end; ++i) {
        if (v[i][col] > num) {
            return true;
        }
    }
    return false;
}

int main (int argc, char const *argv[]) {

    int T, n, m, h;
    cin >> T;
    for (int t = 0; t != T; ++t) {
        cin >> n >> m;
        vector<vector<int> > v(n+2, vector<int>(m+2, 0));
        for (int i = 1; i != n+1; ++i) {
            for (int j = 1; j != m+1; ++j) {
                cin >> v[i][j];
            }
        }
        bool yes = true;
        cout << "Case #" << t+1 << ": ";
        for (int i = 1; i != n+1; ++i) {
            for (int j = 1; j != m+1; ++j) {
                bool r1 = rowHas(v, 0, j, i, v[i][j]);
                bool r2 = rowHas(v, j, m+1, i, v[i][j]);
                bool c1 = colHas(v, 0, i, j, v[i][j]);
                bool c2 = colHas(v, i, n+1, j, v[i][j]);

                if ((r1 && c1) || (r1 && c2) || (r2 && c1) || (r2 && c2)) {
                    yes = false;
                    i = n;
                    break;
                }
            }
        }
        if (yes) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
