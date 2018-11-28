#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <map>


using namespace std;


bool g[101][101];
int b;
long long m;
int used[101];
bool bad = 0;
vector<int> v;
long long cnt[101];
bool tt = 0;
int hu = 0;


void dfs(int i) {
    used[i] = 1;
    for (int j = 0; j < b; j++) {
        if (g[i][j] && used[j] == 1) {
            bad = 1;
        }
        if (g[i][j] && !used[j]) {
            dfs(j);
        }
    }
    used[i] = 2;
    v.push_back(i);
}  


void get(int i, int j) {
    if (tt) {
        return;
    }
    if (i == b) {
        for (int ii = 0; ii < b; ii++) {
            used[ii] = 0;
            cnt[ii] = 0; 
        }
        bad = 0;
        v.clear();
        dfs(0);
        if (!used[b - 1]) {
            bad = 1;
        }
        if (!bad) {
            reverse(v.begin(), v.end());
            for (int ii = 0; ii < (int)v.size(); ii++) {
                int h = v[ii];
                if (h == 0) {
                    cnt[h] = 1;
                }
                for (int jj = 0; jj < b; jj++) {
                    if (g[h][jj]) {
                        cnt[jj] += cnt[h];
                    }
                }
            }
            //cout << cnt[b - 1] << endl;
            if (cnt[b - 1] == m) {
                cout << "Case #" << hu + 1 << ':' << " POSSIBLE" << endl;
                tt = 1;
                for (int ii = 0; ii < b; ii++) {
                    for (int jj = 0; jj < b; jj++) {
                        cout << g[ii][jj];
                    }
                    cout << endl;
                }
            } 
        }
        return;
    }
    if (j == b) {
        get(i + 1, 0);
        return;
    }
    g[i][j] = 0;
    get(i, j + 1);
    if (i != j && g[j][i] == 0) {
        g[i][j] = 1;
        get(i, j + 1);
        g[i][j] = 0;
    }
}


int main() {
    freopen("twopaths.in", "r", stdin);
    freopen("twopaths.out", "w", stdout);
    int t;
    cin >> t;
    for (int ii = 0; ii < t; ii++) {
        cin >> b >> m;
        hu = ii;
        for (int i = 0; i < b; i++) {
            used[i] = 0;
            cnt[i] = 0;
            for (int j = 0; j < b; j++) {
                g[i][j] = 0;
            }
        }
        tt = 0;
        get(0, 0);
        if (!tt) {
            cout << "Case #" << ii + 1 << ':' << " IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
