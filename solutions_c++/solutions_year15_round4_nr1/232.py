#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

char a[123][123];
bool vis[123][123];
int ckr[123], ckc[123];
int R, C, answer;

void readin() {
    scanf("%d%d", &R, &C);
    for (int i = 1; i <= R; ++i)
        scanf("%s", a[i] + 1);
}


bool check_noans() {
    for (int i = 1; i <= R; ++i) ckr[i] = 0;
    for (int i = 1; i <= C; ++i) ckc[i] = 0;
    int cnt = 0;
    for (int i = 1; i <= R; ++i)
        for (int j = 1; j <= C; ++j) if (a[i][j] != '.') {
            bool non = true;
            for (int x = 1; x <= R; ++x) if (x != i) 
                if (a[x][j] != '.') non = 0;
            for (int y = 1; y <= C; ++y) if (y != j)
                if (a[i][y] != '.') non = 0;
            if (non) return true;
        }
    return false;
}

void travel(int i, int j) {
    int dx, dy;
    while (i > 0 && i <= R && j > 0 && j <= C) {
        if (vis[i][j]) return;
        if (a[i][j] != '.') {
            vis[i][j] = 1;
            if (a[i][j] == '^') { dx = -1; dy = 0; } else 
            if (a[i][j] == 'v') { dx = 1; dy = 0; } else 
            if (a[i][j] == '<') { dx = 0; dy = -1; } else 
            if (a[i][j] == '>') { dx = 0; dy = 1; } 
        }
        i += dx; j += dy;
    }
    answer += 1;
}

bool work() {
    if (check_noans()) return false;
    answer = 0;
    for (int i = 1; i <= R; ++i)
        for (int j = 1; j <= C; ++j)
            vis[i][j] = 0;
    for (int i = 1; i <= R; ++i)
        for (int j = 1; j <= C; ++j) 
            if (a[i][j] != '.' && !vis[i][j])
                travel(i, j);
}
    

int main() {
    int task; scanf("%d", &task);
    for (int cas = 1; cas <= task; ++cas) {
        readin();
        printf("Case #%d: ", cas);
        if (work()) {
             printf("%d\n", answer);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}

