#include<stdio.h>
#include<string.h>
int R, C, a[110][110], d[4];
char s[110];
int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};
bool inside(int x, int y) {
    return x >= 0 && x < R && y >= 0 && y < C;
}
void calc(int x, int y, int k) {
    for(;;) {
        x += dx[k], y += dy[k];
        if(!inside(x, y)) {
            return;
        }
        if(a[x][y] != -1) {
            break;
        }
    }
    d[k] = 1;
}
int process() {
    int ans = 0;
    for(int i = 0; i < R; i ++) {
        for(int j = 0; j < C; j ++) {
            if(a[i][j] != -1) {
                memset(d, 0, sizeof(d));
                for(int k = 0; k < 4; k ++) {
                    calc(i, j, k);
                }
                int sum = d[0] + d[1] + d[2] + d[3];
                if(sum == 0) {
                    return -1;
                }
                if(d[a[i][j]] == 0) {
                    ++ ans;
                }
            }
        }
    }
    return ans;
}
int get(char c) {
    if(c == '^') {
        return 0;
    }
    if(c == 'v') {
        return 1;
    }
    if(c == '<') {
        return 2;
    }
    if(c == '>') {
        return 3;
    }
    return -1;
}
int main() {
    //freopen("input.txt", "rb", stdin);
    freopen("A-large.in", "rb", stdin);
    freopen("output.txt", "wb", stdout);
    int t;
    scanf("%d", &t);
    for(int tt= 1; tt <= t; tt ++) {
        scanf("%d%d", &R, &C);
        for(int i = 0; i < R; i ++) {
            scanf("%s", s);
            for(int j = 0; j < C; j ++) {
                a[i][j] = get(s[j]);
            }
        }
        int ans = process();
        if(ans < 0) {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        } else {
            printf("Case #%d: %d\n", tt, ans);
        }
    }
    return 0;
}
