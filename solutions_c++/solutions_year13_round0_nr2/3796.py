#include <stdio.h>
#include <algorithm>

using std::max;

int r[100][100];

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &r[i][j]);

        bool fail = false;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                int z = 0;
                for (int k = 0; k < m; k++)
                    z = max(z, r[i][k]);

                if (z == r[i][j])
                    continue;

                z = 0;
                for (int k = 0; k < n; k++)
                    z = max(z, r[k][j]);

                if (z != r[i][j])
                    fail = true;
            }

        printf("Case #%d: ", i);
        if (fail)
            printf("NO\n");
        else
            printf("YES\n");
    }

    return 0;
}
