#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool checkLane(int r, int c, vector<vector<int> > &v) {
    bool okHori = true;
    // check row
    for (int i = 0; i < v[0].size(); ++i) {
        if (v[r][i] != v[r][c]) okHori = false;
    }

    bool okVert = true;
    // check col
    for (int i = 0; i < v.size(); ++i) {
        if (v[i][c] != v[r][c]) okVert = false;
    }

    return okVert | okHori;
}

bool heightOK(int currentHeight, vector<vector<int> > &v) {
    for (int i = 0; i < v.size(); ++i) {
        for (int j = 0; j < v[0].size(); ++j) {
            if (v[i][j] == currentHeight) {
                if (!checkLane(i,j,v)) return false;
            }
        }
    }
    return true;
}

bool works(vector<vector<int> > &v) {
    for (int curH = 1; curH <= 99; ++curH) {
        if (!heightOK(curH,v)) return false;
        for (int i = 0; i < v.size(); ++i) {
            for (int j = 0; j < v[0].size(); ++j) {
                v[i][j] = max(v[i][j],curH+1);
            }
        }
    }
    return true;
}

void solve() {
    int R,C;
    cin >> R >> C;
    vector<vector<int> > lawn(R,vector<int>(C));
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            cin >> lawn[i][j];
        }
    }
    if (works(lawn)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
}
