#include <cstdio>
#include <cstring>
const int maxr = 1000;
const int maxc = 1000;
const int INF = 0x3fffffff;
bool maze[maxr][maxc];
int r, c, n, ans;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
bool test(int x, int y) {
    if(x <= 0 || x > r || y <= 0 || y > c) return false;
    if(maze[x][y] == 1) return true;
    else return false;
}
void DFS(int indexX, int indexY, int num) {
    if(num == n) {
        int temp = 0;
        for(int i = 1; i <= r; i++) {
            for(int j = 1; j <= c; j++) {
                if(maze[i][j] == 1) {
                    for(int k = 0; k < 4; k++) {
                        int newX = i + dx[k];
                        int newY = j + dy[k];
                        if(test(newX, newY)) {
                            temp++;
                        }
                    }
                }
            }
        }
        temp /= 2;
        if(temp < ans) {
            ans = temp;
        }
        return;
    }
    if(indexX > r) {
        return;
    }
    maze[indexX][indexY] = 1;
    if(indexY < c) {
        DFS(indexX, indexY + 1, num + 1);
    } else {
        DFS(indexX + 1, 1, num + 1);
    }
    maze[indexX][indexY] = 0;
    if(indexY < c) {
        DFS(indexX, indexY + 1, num);
    } else {
        DFS(indexX + 1, 1, num);
    }
}
int main() {
    int T, tcase = 1;
    scanf("%d", &T);
    while(T--) {
        memset(maze, 0, sizeof(maze));
        scanf("%d%d%d", &r, &c, &n);
        ans = INF;
        DFS(1, 1, 0);
        printf("Case #%d: %d\n", tcase++, ans);
    }
    return 0;
}
