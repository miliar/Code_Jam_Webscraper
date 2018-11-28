#include <cstdio>

using namespace std;

int rows[100], cols[100];

int main() {
    FILE *out = fopen("out.txt", "w");

    int T, N, M;
    scanf("%d", &T);

    for (int k = 0; k < T; k++) {
        scanf("%d %d", &N, &M);
        int map[N][M];

        for (int i = 0; i < N; i++) {
            rows[i] = -1;
        }

        for (int i = 0; i < M; i++) {
            cols[i] = -1;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                scanf("%d", &map[i][j]);

                if (rows[i] == -1 || map[i][j] > rows[i]) {
                    rows[i] = map[i][j];
                }

                if (cols[j] == -1 || map[i][j] > cols[j]) {
                    cols[j] = map[i][j];
                }
            }
        }

        bool exit = false;
        for (int r = 0; r < N && !exit; r++) {
            for (int c = 0; c < M && !exit; c++) {
                if (map[r][c] < rows[r] && map[r][c] < cols[c]) {
                    fprintf(out, "Case #%d: NO\n", k + 1);
                    exit = true;
                }
            }
        }

        if (!exit) {
            fprintf(out, "Case #%d: YES\n", k + 1);
        }
    }

    return 0;
}

