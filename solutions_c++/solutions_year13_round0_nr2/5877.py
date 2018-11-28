#include <iostream>
#include <cstdio>

using namespace std;

int movn[109][109];
int rows[109], cols[109];

int main() {

    int t, n, m;

    scanf("%d", &t);

    for (int i = 1; i <= t; ++i) {

        scanf("%d %d", &n, &m);

        for (int j = 0; j < n; ++j)
            for (int k = 0; k < m; ++k)
                scanf("%d", &movn[j][k]);

        for (int j = 0; j < n; ++j) {
            int maxi = 0;
            for (int k = 0; k < m; ++k)
                maxi = max(maxi, movn[j][k]);
            cols[j] = maxi;
        }

        for (int k = 0; k < m; ++k) {
            int maxi = 0;
            for (int j = 0; j < n; ++j)
                maxi = max(maxi, movn[j][k]);
            rows[k] = maxi;
        }

        bool res = true;

        for (int j = 0; j < n; ++j)
            for (int k = 0; k < m; ++k)
                if (movn[j][k] < cols[j] && movn[j][k] < rows[k]) {
                    res = false;
                    break;
                }

        printf("Case #%d: %s\n", i, (res ? "YES" : "NO"));
    }

    return 0;
}

