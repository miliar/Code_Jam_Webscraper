#include <cstdio>

int buf[200][200];
int m;
int n;

int checkx(int y, int val)
{
    for (int i = 0; i < n; ++i) {
        if (buf[i][y] > val) {
            return 0;
        }
    }
    return 1;
}

int checky(int x, int val)
{
    for (int i = 0; i < m; ++i) {
        if (buf[x][i] > val) {
            return 0;
        }
    }
    return 1;
}

int status()
{
    /* find min */
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!checkx(j, buf[i][j]) && !checky(i, buf[i][j])) {
                return 0;
            }
        }

    }
    return 1;
}

int main()
{
    FILE * fd = fopen("input", "r");
    int testnum;
    fscanf(fd, "%d ", &testnum);

    for (int test = 1; test <= testnum; ++test) {
        fscanf(fd, "%d %d ", &n, &m);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                fscanf(fd, "%d", &buf[i][j]);
            }
        }

        int rv = status();
        if (rv) {
            printf("Case #%d: YES\n", test);
        } else {
            printf("Case #%d: NO\n", test);
        }
    }
}

