#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        int r1, r2;
        int a[5][5], b[5][5];
        cin >> r1;
        for (int i = 1; i <= 4;++i)
            for (int j = 1; j <= 4; ++j)
                cin >> a[i][j];
        cin >> r2;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                cin >> b[i][j];
        int ans = 0, ans_ = 0;
        for (int i = 1; i <= 4;++i) {
            int ok = false;
            for (int j = 1; j <= 4; ++j)
                if (a[r1][i] == b[r2][j]) ok = true, ans_ = a[r1][i];
            if (ok) ans++;
        }
        printf("Case #%d: ", ++ca);
        if (ans == 0) puts("Volunteer cheated!");
        if (ans > 1) puts("Bad magician!");
        if (ans == 1) printf("%d\n", ans_);
    }
    return 0;
}
