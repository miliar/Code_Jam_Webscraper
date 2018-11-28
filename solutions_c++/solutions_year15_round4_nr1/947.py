#include <bits/stdc++.h>
using namespace std;

int r, c;
string a[1000];

bool find(int x, int y, int dx, int dy) {
    int i = y + dy, j = x + dx;
    while (i >= 0 && i < r && j >= 0 && j < c && a[i][j] == '.') {
        i += dy;
        j += dx;
    }
    return i >= 0 && i < r && j >= 0 && j < c;
}

int main () {
    int t;
    cin >> t;
    for (int qq = 1; qq <= t; ++qq) {
        cin >> r >> c;
        for (int i = 0; i < r; ++i) cin >> a[i];
        int ans = 0;
        for (int i = 0; ans >= 0 && i < r; ++i) {
            for (int j = 0; ans >= 0 && j < c; ++j) {
                bool ok = false;
                switch (a[i][j]) {
                    case '^': ok = find(j, i, 0, -1); break;
                    case '>': ok = find(j, i, 1, 0); break;
                    case '<': ok = find(j, i, -1, 0); break;
                    case 'v': ok = find(j, i, 0, 1); break;
                    default: ok = true;
                }

                if (ok) continue;

                if (find(j, i, 0, -1) || find(j, i, 1, 0) || find(j, i, -1, 0) || find(j, i, 0, 1)) ++ans;
                else ans = -1;
            }
        }

        cout << "Case #" << qq << ": ";
        if (ans >= 0) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
