#include <stdio.h>
#include <algorithm>

bool solve() {
    static int H[100][100], MH[100], MV[100];
    int n, m;
    scanf("%d %d", &n, &m);
    std::fill(MV, MV + m, 0);
    for (int i = 0; i < n; i++) {
        MH[i] = 0;
        for (int j = 0; j < m; j++) {
            scanf("%d", &H[i][j]);
            MH[i] = std::max(MH[i],H[i][j]);
            MV[j] = std::max(MV[j], H[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (H[i][j] != MV[j] && H[i][j] != MH[i])
                return false;
        }
    }
    return true;
}

int main() {
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; i++)
        printf("Case #%d: %s\n", i, solve() ? "YES" : "NO");
    return 0;
}
