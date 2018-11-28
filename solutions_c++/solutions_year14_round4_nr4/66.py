#include <set>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
string s[1024];
vector<string> t[8];
int ans, res;

void read() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
}

int calc() {
    int ans = 0;
    
    for (int i = 0; i < m; i++) {
        set<string> s;
        for (int j = 0; j < (int)t[i].size(); j++) {
            string p = t[i][j];
            
            for (int k = 0; k <= (int)p.size(); k++) {
                s.insert(p.substr(0, k));
            }
        }
        
        ans += (int)s.size();
    }
    return ans;
}

void go(int x) {
    if (x == n) {
        int nodes = calc();
        if (nodes > ans) {
            ans = nodes;
            res = 1;
        } else {
            if (nodes == ans) {
                ++ res;
            }
        }
        return ;
    }
    for (int j = 0; j < m; j++) {
        t[j].push_back(s[x]);
        go(x + 1);
        t[j].pop_back();
    }
}

void solve() {
    ans = res = -1;
    for (int j = 0; j < m; j++) t[j].clear();
    go(0);
    
    printf ("%d %d\n", ans, res);
}

int main() {
    int cases;
    
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
