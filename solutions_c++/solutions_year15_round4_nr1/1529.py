#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

#define LL long long

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<char> vc;
typedef vector<vc> vvc;

int R, C;
vvc v;
vvi mem;

int F(int x, int y) {
    if (v[x][y] == '^') {
        for (int i = x-1; i >= 0; --i) {
            if (v[i][y] != '.') return 0;
        }
        return 1;
    }
    if (v[x][y] == 'v') {
        for (int i = x+1; i < R; ++i) {
            if (v[i][y] != '.') return 0;
        }
        return 1;
    }
    if (v[x][y] == '<') {
        for (int i = y-1; i >= 0; --i) {
            if (v[x][i] != '.') return 0;
        }
        return 1;
    }
    if (v[x][y] == '>') {
        for (int i = y+1; i < C; ++i) {
            if (v[x][i] != '.') return 0;
        }
        return 1;
    }
    return 0;
}
bool F2(int x, int y) {
    if (v[x][y] == '.') return true;
   for (int i = x-1; i >= 0; --i) {
            if (v[i][y] != '.') return true;
        }

   for (int i = x+1; i < R; ++i) {
            if (v[i][y] != '.') return true;
        }
   
    for (int i = y-1; i >= 0; --i) {
            if (v[x][i] != '.') return true;
        }
    
    for (int i = y+1; i < C; ++i) {
        if (v[x][i] != '.') return true; 
    }
    return false; 
}

int main(int argc, char** argv) {
    int T;
    cin >> T;
    for (int cases = 1; cases <= T; ++cases) {
    cin >> R >> C;
    v = vvc(R, vc(C));
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            cin >> v[i][j];
    int ans = 0;
    bool possible = true;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) {
            ans += F(i, j);
            possible &= F2(i, j);
        }
    cout << "Case #" << cases << ": ";
    if (possible)
        cout << ans << endl;
    else
        cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}

