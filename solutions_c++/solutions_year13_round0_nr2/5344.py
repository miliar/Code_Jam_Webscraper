#include <cstdio>

int M[105][105];
int G[105][105];

void go(bool& cut, int y, int x, int dy, int dx, int ny, int nx, int high) {
    if(y >= 1 && y <= ny && x >= 1 && x <= nx) {
        if(y == ny || x == nx) {
            cut = true;
        } else if(high == 0) {
            go(cut, y + dy, x + dx, dy, dx, ny, nx, M[y][x]);
        } else if(M[y][x] == high) {
            go(cut, y + dy, x + dx, dy, dx, ny, nx, high);
        }
    }
}

int main() {
    int T, cases = 0;;
    scanf("%d", &T);
    while(T-- > 0) {
        printf("Case #%d: ", (++cases));
        int ny, nx, highest = -1;
        scanf("%d%d", &ny, &nx);
        for(int i = 1; i <= ny; ++i) {
            for(int j = 1; j <= nx; ++j) {
                scanf("%d", &M[i][j]);
                if(highest < M[i][j]) {
                    highest = M[i][j];
                }
            }
        }
        for(int i = 1; i <= ny; ++i) {
            for(int j = 1; j <= nx; ++j) {
                G[i][j] = highest;
            }
        }
        for(int i = 1; i <= ny; ++i) {
            bool cut = false;
            go(cut, i, 1, 0, +1, ny + 1, nx + 1, 0);
            if(cut) {
                for(int j = 1; j <= nx; ++j) {
                    G[i][j] = M[i][j];
                }
            }
        }
        for(int i = 1; i <= nx; ++i) {
            bool cut = false;
            go(cut, 1, i, +1, 0, ny + 1, nx + 1, 0);
            if(cut) {
                for(int j = 1; j <= ny; ++j) {
                    G[j][i] = M[j][i];
                }
            }
        }
        bool answer = true;
        for(int i = 1; i <= ny; ++i) {
            for(int j = 1; j <= nx; ++j) {
                if(G[i][j] != M[i][j]) {
                    answer = false;
                    goto THE_END;
                }
            }
        }
THE_END:
        puts((answer ? "YES" : "NO"));
    }
    return 0;
}
