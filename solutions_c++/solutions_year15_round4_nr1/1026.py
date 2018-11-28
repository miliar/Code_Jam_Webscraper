//#include "testlib.h"

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <map>
#include <vector>
#include <stdlib.h>
#include <memory.h>
#include <time.h>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <cassert>
#include <queue>
#include <numeric>

using namespace std;

string s[111];
int go[111][111];
int n, m;

int dx[] = {0, -1, 0, 1, 0};
int dy[] = {0, 0, 1, 0, -1};

bool norm(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        int ans = 0;
        bool bad = 0;
        cin >> n >> m;
        for(int i = 0; i < n; ++i) {
            cin >> s[i];
            for(int j = 0; j < m; ++j)
            if (s[i][j] == '^')
                go[i][j] = 1;
            else if (s[i][j] == '>')
                go[i][j] = 2;
            else if (s[i][j] == 'v')
                go[i][j] = 3;
            else if (s[i][j] == '<')
                go[i][j] = 4;
            else
                go[i][j] = 0;
        }
        
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
            if (go[i][j] != 0) {
                int x = i;
                int y = j;
                bool f = 0;
                while (!f) {
                    x += dx[go[i][j]];
                    y += dy[go[i][j]];
                    if (!norm(x, y)) break;
                    if (go[x][y] != 0)
                        f = 1;
                }
                
                bool f2 = 0;
                for(int to = 1; to <= 4; ++to)
                if(to != go[i][j]) {
                    x = i;
                    y = j;
                    while (!f2) {
                        x += dx[to];
                        y += dy[to];
                        if (!norm(x, y)) break;
                        if (go[x][y] != 0)
                            f2 = 1;
                    }
                }
                
                if (!f) {
                    ans++;
                    if (!f2)
                        bad = 1;
                }
            }
        
        
        cout << "Case #" << t << ": ";
        if (bad)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
    return 0;
}