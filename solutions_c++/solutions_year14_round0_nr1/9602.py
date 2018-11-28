#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t, x, m[5][5], v[20], l, r, val;

int main() {
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);

    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        memset(v, 0, sizeof(v));
        l = r = 0;
        cin >> x;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) cin >> m[i][j];
        for (int j = 1; j <= 4; j++) v[m[x][j]]++;
        cin >> x;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) cin >> m[i][j];
        for (int j = 1; j <= 4; j++) v[m[x][j]]++;
        for (int i = 1; i <= 16; i++)
            if (v[i] == 1) l++; else
            if (v[i] == 2) {r++; val = i;}
        if (r == 0) printf("Case #%d: Volunteer cheated!\n", tt); else
        if (r == 1) printf("Case #%d: %d\n", tt, val); else
            printf("Case #%d: Bad magician!\n", tt);
    }

    return 0;
}
