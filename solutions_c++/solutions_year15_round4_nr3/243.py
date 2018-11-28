#include <cstdio>
#include <sstream>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

map<string, int> mp;
int ee;

int n;
vector<int> a[32];

int def[1024 * 256];

int getidx(string s) {
    if (mp.find(s) != mp.end()) {
        return mp[s];
    }
    mp[s] = ++ ee;
    return mp[s];
}

void read() {
    cin >> n;

    ee = 0;
    mp.clear();

    string q, w;
        getline(cin, q);
    for (int i = 0; i < n; i++) {
        a[i].clear();

        getline(cin, q);
        istringstream in(q);
        while (in >> w) {
            a[i].push_back(getidx(w));
        }
    }
}

void solve() {
    int ans = 1 << 30;
    for (int i = 0; i < (1 << (n - 2)); i++) {
        for (int j = 1; j <= ee; j++) def[j] = 0;

        for (int j = 0; j < (int)a[0].size(); j++) def[ a[0][j] ] |= 1;
        for (int j = 0; j < (int)a[1].size(); j++) def[ a[1][j] ] |= 2;
    
        for (int j = 0; j < n - 2; j++) {
            for (int k = 0; k < (int)a[2 + j].size(); k++) {
                def[ a[2 + j][k] ] |= (1 + !!(i & (1 << j)));
            }
        }

        int cur = 0;
        for (int j = 1; j <= ee; j++) {
            if (def[j] == 3) cur ++;
        }
        if (cur < ans) ans = cur;
    }

    printf ("%d\n", ans);
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
