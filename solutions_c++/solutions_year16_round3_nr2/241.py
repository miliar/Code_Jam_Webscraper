#include <bits/stdc++.h>

using namespace std;

int T, B;

long long M;

bool res[55][55];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> B >> M;
        memset(res, 0, sizeof res);
        int i;
        for (i = 63; i >= 0; --i)
            if (M & (1ll << i)) {
                for (int u = 1; u <= i + 2; ++u) {
                    for (int v = u + 1; v <= i + 2; ++v) {
                        res[u][v] = 1;
                    }
                }
                break;
            }
        if ((M ^ (1ll << i)) == 0 && i + 2 == B) {
            cout << "Case #" << t << ": POSSIBLE\n";
            for (int u = 1; u <= B; ++u) {
                for (int v = 1; v <= B; ++v) {
                    printf("%d", res[u][v]);
                }
                puts("");
            }
            continue;
        }
        if (i + 3 > B) {
            cout << "Case #" << t <<": IMPOSSIBLE\n";
            continue;
        }

        res[i + 2][B] = 1;
        for (i = i - 1; i >= 0; --i)
            if (M & (1ll << i))
                    res[i + 2][B] = 1;
            cout << "Case #" << t << ": POSSIBLE\n";
            for (int u = 1; u <= B; ++u) {
                for (int v = 1; v <= B; ++v) {
                    printf("%d", res[u][v]);
                }
                puts("");
            }
    }
}
