#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define REP(i,n) FOR(i,0,n)
#define DBGV(_v) { REP(_i, _v.sz) { cout << _v[_i] << "\t";} cout << endl;}
#define sz size()

using namespace std;

bool isRowPossible(vector <vector <int > > grid, int x, int y) {
    REP(i, grid.size()) {
        if (grid[i][y] > grid[x][y]) {
            return false;
        }
    }
    return true;
}

bool isColPossible(vector <vector <int > > grid, int x, int y) {
    REP(i, grid[0].size()) {
        if (grid[x][i] > grid[x][y]) {
            return false;
        }
    }
    return true;
}

bool isPossible(vector <vector <int> > grid) {
    REP(i, grid.size()) {
        REP(j, grid[0].size()) {
            if (isRowPossible(grid, i, j) == false && isColPossible(grid, i, j) == false) {
                return false;
            }
        }
    }
    return true;
}


int main() {
    int kase = 0;
    cin >> kase;
    for(int kase_cnt = 1; kase_cnt <= kase; kase_cnt++) {
        int m, n;
        vector <vector < int> > grid;
        cin >> m >> n;
        REP(i, m) {
            vector <int> tmp;
            REP(j, n) {
                int t;
                cin >> t;
                tmp.push_back(t);
            }
            grid.push_back(tmp);
        }

        cout << "Case #" << kase_cnt << ": ";
        if (isPossible(grid)) {
            cout << "YES";
        }
        else {
            cout << "NO";
        }
        cout << endl;
    }
}
