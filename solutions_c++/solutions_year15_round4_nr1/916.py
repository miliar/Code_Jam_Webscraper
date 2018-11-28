#include <bits/stdc++.h>

#define DBG(x)

using namespace std;

char c[100][100];
int lr[100][100], td[100][100];

int main() {
    int T, t, ans, R, C;
    bool fail;
    scanf("%d", &T);
    for(t = 0; t < T; ++t) {
        ans = 0;
        fail = false;
        scanf("%d %d", &R, &C);
        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                scanf(" %c", &c[i][j]);
                lr[i][j] = td[i][j] = 0;
            }
        }
        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                if(c[i][j] != '.') {
                    if(j > 0) {
                        lr[i][j] = lr[i][j-1] + 1;
                    } else {
                        lr[i][j] = 1;
                    }
                    if(i > 0) {
                        td[i][j] = td[i-1][j] + 1;
                    } else {
                        td[i][j] = 1;
                    }
                } else {
                    if(j > 0) {
                        lr[i][j] = lr[i][j-1];
                    } else {
                        lr[i][j] = 0;
                    }
                    if(i > 0) {
                        td[i][j] = td[i-1][j];
                    } else {
                        td[i][j] = 0;
                    }
                }
            }
        }
        DBG(
        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                printf("%d ", lr[i][j]);
            }
            printf("\n");
        }
        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                printf("%d ", td[i][j]);
            }
            printf("\n");
        })
        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                if(c[i][j] != '.') {
                    if(lr[i][C-1] == 1 && td[R-1][j] == 1) {
                        fail = true;
                        break;
                    }
                    switch(c[i][j]) {
                        case '>':
                            if(lr[i][C-1]-lr[i][j] == 0) ++ans;
                            break;
                        case '<':
                            if(lr[i][j] == 1) ++ans;
                            break;
                        case '^':
                            if(td[i][j] == 1) ++ans;
                            break;
                        case 'v':
                            if(td[R-1][j]-td[i][j] == 0) ++ans;
                            break;
                    }
                }
            }
            if(fail) break;
        }
        if(fail) {
            printf("Case #%d: IMPOSSIBLE\n", t+1);
        } else {
            printf("Case #%d: %d\n", t+1, ans);
        }
    }
}
