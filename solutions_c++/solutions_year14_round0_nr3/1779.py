#include <algorithm>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int MAX_SIZE = 100; 

int R, C, M;
bool found = false;
char grid[MAX_SIZE][MAX_SIZE];
int neig[MAX_SIZE][MAX_SIZE];
bool vis[MAX_SIZE][MAX_SIZE];

int difx[8] = {-1,  0,  1, 1, 1, 0, -1, -1};
int dify[8] = {-1, -1, -1, 0, 1, 1,  1,  0};

int dfs(int y, int x) {
    vis[y][x] = true;
    if (neig[y][x] > 0)
        return 1;

    int visited = 1;
    for (int d = 0; d < 8; ++d) {
        int ny = y + dify[d];
        int nx = x + difx[d];
        if (ny < 0 || ny >= R)
            continue;
        if (nx < 0 || nx >= C)
            continue;
        if (vis[ny][nx])
            continue;
        visited += dfs(ny, nx);
    }
    return visited;
}

void search(int y, int x, int mines) {
    if (x == C) {
        search(y+1, 0, mines);
    } else if (mines == 0) {
        /*
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                printf("%c", grid[i][j]);
            printf("\n");
        } printf("mines: %d\n\n", mines);
*/
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j) {
                neig[i][j] = 0;
                vis[i][j] = 0;
            }

        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j)
                if (grid[i][j] == '*') {
                    neig[i][j] += 10;
                    for (int d = 0; d < 8; ++d) {
                        int ni = i + dify[d];
                        int nj = j + difx[d];
                        if (ni < 0 || ni >= R)
                            continue;
                        if (nj < 0 || nj >= C)
                            continue;
                        neig[ni][nj]++;
                    }
                }

        /*
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                printf("%c", grid[i][j]);
            printf("\n");
        }
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                printf("%3d ", neig[i][j]);
            printf("\n");
        } printf("\n");
        */

        // check current grid
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (neig[i][j] != 0)
                    continue;
                grid[i][j] = 'c';
                int visited = dfs(i, j);
                //printf("visited: %d\n", visited);
                if (visited == R*C-M)
                    found = true;
                else
                    grid[i][j] = '.';
                return;
            }
        }
    } else {
        int start = x;
        for (int i = y; i < R; ++i) {
            for (int j = start; j < C; ++j) {
                grid[i][j] = '*';
                search(i, j+1, mines-1);
                if (found)
                     return;
                grid[i][j] = '.';
            }
            start = 0;
        }
    }
}

int main(int argc, char *argv[]) {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d%d", &R, &C, &M);
        bool swapped = false;
        if (swapped)
            swap(R, C);
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j)
                grid[i][j] = '.';

        found = false;
        search(0, 0, M);
        printf("Case #%d:\n", t);

        if (!found && M == R*C-1) {
            for (int i = 0; i < R; ++i)
                for (int j = 0; j < C; ++j)
                    grid[i][j] = '*';
            grid[0][0] = 'c';
            found = true;
        }
        if (found) {
            if (swapped) {
                for (int i = 0; i < R; ++i) {
                    for (int j = 0; j < C; ++j) {
                        printf("%c", grid[j][i]); 
                    }
                    printf("\n");
                }
 
            } else {
                for (int i = 0; i < R; ++i) {
                    for (int j = 0; j < C; ++j) {
                        printf("%c", grid[i][j]); 
                    }
                    printf("\n");
                }
            }
        } else
            printf("Impossible\n");
    }
    return EXIT_SUCCESS;
}
