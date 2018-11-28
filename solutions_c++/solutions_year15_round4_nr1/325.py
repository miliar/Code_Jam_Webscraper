#include <cstdio>
#include <cstring>

int n, m;
int a[128][128];
int r[128];
int c[128];

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

void read() {
    scanf("%d%d", &n, &m);
    memset(r, 0, sizeof r);
    memset(c, 0, sizeof c);

    for (int i = 0; i < n; i++) {
        char buf[128];

        scanf("%s", buf);
        for (int j = 0; j < m; j++) {
            int e;
            if (buf[j] == '.') e = 4;
            if (buf[j] == '^') e = 0;
            if (buf[j] == '>') e = 1;
            if (buf[j] == 'v') e = 2;
            if (buf[j] == '<') e = 3;
            a[i][j] = e;
            r[i] += (e != 4);
            c[j] += (e != 4);
        }
    }
}

int solve() {
    int ans = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != 4) {
                if (r[i] == 1 && c[j] == 1) return 0;

                int dir = a[i][j];
                int x = i + dx[dir];
                int y = j + dy[dir];

                while (x >= 0 && y >= 0 && x < n && y < m && a[x][y] == 4) {
                    x += dx[dir];
                    y += dy[dir];
                }

                if (!(x >= 0 && y >= 0 && x < n && y < m)) {
                    ++ ans;
                }
            }
        }
    }

    printf ("%d\n", ans);

    return 1;
}

int main() {
    int i, cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        if (!solve()) {
            printf ("IMPOSSIBLE\n");
        }
    }
    
    return 0;
}
