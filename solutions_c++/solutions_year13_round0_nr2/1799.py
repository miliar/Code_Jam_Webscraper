#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Grid: public vector<vector<int> > {
public:
    Grid () {
    }
    
    Grid (int n, int m): vector<vector<int> >(n, vector<int>(m)) {
    }
};


Grid readGrid (istream & in) {
    int n, m;
    in >> n >> m;
    Grid a(n, m);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            in >> a[i][j];
        }
    }
    return a;
}

const int MIN_H = 1,
          MAX_H = 100;

bool canReach (Grid const & a) {
    int n = a.size(), m = a[0].size();
    vector<bool> canTouchX(n, true), canTouchY(m, true);
    
    for (int h = MAX_H; h >= MIN_H; --h) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] <= h && (!canTouchX[i] && !canTouchY[j])) {
                    return false;
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] == h) {
                    canTouchX[i] = false;
                    canTouchY[j] = false;
                }
            }
        }
    }
    
    return true;
}

void solveCase (int caseNum) {
    Grid a(readGrid(cin));
    cout << "Case #" << caseNum + 1 << ": " << (canReach(a) ? "YES" : "NO") << "\n";
}

int main () {
    int testsCount;
    cin >> testsCount;
    for (int i = 0; i < testsCount; ++i) {
        solveCase(i);
    }
    return 0;
}
