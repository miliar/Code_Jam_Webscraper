#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

#define pairii pair<int, int>
#define llong long long
#define pb push_back
#define sortall(x) sort((x).begin(), (x).end())
#define INFI  numeric_limits<int>::max()
#define INFL  numeric_limits<long>::max()
#define INFLL numeric_limits<llong>::max()
#define INFD  numeric_limits<double>::max()
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

void minesweeper(vector<string>& res, int r, int c, int m) {
    if (c < r) {
        if (m >= c) {
            minesweeper(res, r-1, c, m-c);
            res.pb(string(c,'*'));
            return;
        }
    }
    else {
        if (m >= r) {
            minesweeper(res, r, c-1, m-r);
            FORZ(i,r) res[i].pb('*');
            return;
        }
    }
    
    vector<string> board(r);
    FORZ(i,r) board[i] = string(c,'.');
    int cnt = 0;
    for (int j = c-1; j >= 2 && cnt < m; j--) {
        board[r-1][j] = '*';
        cnt++;
    }
    for (int i = r-2; i >= 2 && cnt < m; i--) {
        board[i][c-1] = '*';
        cnt++;
    }
    if (cnt < m && r > c) board[1][c-1] = '*';
    else if (cnt < m) board[r-1][1] = '*';
    res = board;
    
}

void solve() {
    int r,c,m; cin >> r >> c >> m;
    vector<string> board;
    minesweeper(board, r, c, m);
    
    queue<pairii> q;
    q.push(make_pair(0, 0));
    while (!q.empty()) {
        pairii pos = q.front();
        q.pop();
        board[pos.first][pos.second] = 'v';
        int cnt = 0;
        FOR(i,pos.first-1,pos.first+2) FOR(j,pos.second-1,pos.second+2) {
            if (i >= 0 && i < r && j >= 0 && j < c && board[i][j] != 'v') {
                if (board[i][j] == '*') cnt++;
            }
        }
        if (cnt == 0) {
            FOR(i,pos.first-1,pos.first+2) FOR(j,pos.second-1,pos.second+2) {
                if (i >= 0 && i < r && j >= 0 && j < c && board[i][j] != 'v') {
                    q.push(make_pair(i, j));
                }
            }
        }
    }
    
    bool possible = true;
    
    FORZ(i,r) FORZ(j,c) {
        if (board[i][j] == '.') {
            possible = false;
            break;
        }
    }
    
    /*
     FORZ(i,r) {
     FORZ(j,c) {
     cout << board[i][j];
     }
     cout << endl;
     }
     */
    
    if (possible) {
        FORZ(i,r) {
            FORZ(j,c) {
                if (i == 0 && j == 0) board[i][j] = 'c';
                else if (board[i][j] != '*') board[i][j] = '.';
                else board[i][j] = '*';
            }
        }
    }
    
    if (possible) {
        FORZ(i,r) {
            cout << board[i] << endl;
        }
    }
    else {
        cout << "Impossible\n";
    }
}

int main() {
#ifdef DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t; cin >> t;
    FORZ(i,t) {
        cout << "Case #" << i+1 << ":\n";
        solve();
    }

    return 0;
}
