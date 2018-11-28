#include <bits/stdc++.h>

const int N = 100 + 5;
char str[N][N];
int n,m;
int tag[N][N];

bool in_range(int x,int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

bool work() {
    memset(tag,0,sizeof(tag));
    for (int i = 0; i < m; ++ i) {
        int x = 0,y = i;
        int dx = 1,dy = 0;
        while (in_range(x,y) && str[x][y] == '.') {
            x += dx;
            y += dy;
        }
        if (in_range(x,y)) {
            tag[x][y] |= 1 << 0;
        }
    }
    for (int i = 0; i < m; ++ i) {
        int x = n - 1,y = i;
        int dx = -1,dy = 0;
        while (in_range(x,y) && str[x][y] == '.') {
            x += dx;
            y += dy;
        }
        if (in_range(x,y)) {
            tag[x][y] |= 1 << 1;
        }
    }
    for (int i = 0; i < n; ++ i) {
        int x = i,y = 0;
        int dx = 0,dy = 1;
        while (in_range(x,y) && str[x][y] == '.') {
            x += dx;
            y += dy;
        }
        if (in_range(x,y)) {
            tag[x][y] |= 1 << 2;
        }
    }
    for (int i = 0; i < n; ++ i) {
        int x = i,y = m - 1;
        int dx = 0,dy = -1;
        while (in_range(x,y) && str[x][y] == '.') {
            x += dx;
            y += dy;
        }
        if (in_range(x,y)) {
            tag[x][y] |= 1 << 3;
        }
    }
    int ret = 0;
    for (int i = 0; i < n; ++ i) {
        for (int j = 0; j < m; ++ j) {
            if (str[i][j] == '.') continue;
            if (tag[i][j] == (1 << 4) - 1) {
                return false;
            }
            if (str[i][j] == '^' && (tag[i][j] >> 0 & 1)
                    || str[i][j] == 'v' && (tag[i][j] >> 1 & 1)
                    || str[i][j] == '>' && (tag[i][j] >> 3 & 1)
                    || str[i][j] == '<' && (tag[i][j] >> 2 & 1))
                ret ++;
        }
    }
    printf("%d\n",ret);
    return true;
}

int main(int argc,char **args) {
    if (argc > 1) {
        freopen(args[1],"r",stdin);
        freopen("data.txt","w",stdout);
    }
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; ++ i) {
            scanf("%s",str[i]);
        }
        printf("Case #%d: ",++ca);
        if (!work()) {
            puts("IMPOSSIBLE");
        }
    }
}
