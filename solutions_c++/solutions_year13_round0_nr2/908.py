#include <cstdio>
using namespace std;

int main() {
    int T, N, M;
    int grid[100][100];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                scanf("%d", &grid[i][j]);

        bool ok = 1;
        for (int i = 0; ok && i < N; i++) {
            for (int j = 0; ok && j < M; j++) {
                bool ok1 = 1, ok2 = 1;
                for (int k = 0; k < N; k++)
                    if (grid[k][j] > grid[i][j])
                        ok1 = 0;
                for (int k = 0; k < M; k++)
                    if (grid[i][k] > grid[i][j])
                        ok2 = 0;
                ok = ok1 || ok2;
            }
        }
        printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
    }
}
