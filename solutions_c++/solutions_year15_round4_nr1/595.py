#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

void solve() {
    int r, c;
    cin >> r >> c;
    
    vector<string> v;
    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        v.push_back(s);
    }
    
    int cnt = 0;
    
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            bool hasBorder[4] = {0};
            for (int k = i - 1; k >= 0; k--) {
                if (v[k][j] != '.') {
                    hasBorder[0] = true;
                }
            }
            for (int k = i + 1; k < r; k++) {
                if (v[k][j] != '.') {
                    hasBorder[1] = true;
                }
            }
            for (int k = j + 1; k < c; k++) {
                if (v[i][k] != '.') {
                    hasBorder[2] = true;
                }
            }
            for (int k = j - 1; k >= 0; k--) {
                if (v[i][k] != '.') {
                    hasBorder[3] = true;
                }
            }
            if (v[i][j] == '^' && !hasBorder[0] ||
                v[i][j] == 'v' && !hasBorder[1] ||
                v[i][j] == '>' && !hasBorder[2] ||
                v[i][j] == '<' && !hasBorder[3]) {
                if (!hasBorder[0] && !hasBorder[1] && !hasBorder[2] && !hasBorder[3]) {
                    cout << "IMPOSSIBLE";
                    return;
                }
                cnt++;
            }
        }
    }
    
    cout << cnt;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("A-large.in-3.txt", "rt", stdin);
//    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
}
