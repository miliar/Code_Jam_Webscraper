#include <bits/stdc++.h>
using namespace std;

int bit(int k, int i) {
    return (k >> i) & 1;
}

int f[20][20][20];

int task1(int r, int c, int n) {
    if (f[r][c][n] == -1) {
        f[r][c][n] = 1e9;
        for (int i = 0; i < (1 << (r * c)); i++) {
            int count = 0, unhappy = 0;
            for (int j = 0; j < r * c; j++)
                if (bit(i, j)) {
                    count++;
                    if (j % c > 0 && bit(i, j - 1))
                        unhappy++;
                    if (j - c >= 0 && bit(i, j - c))
                        unhappy++;
                }
            if (count == n) {
                f[r][c][n] = min(f[r][c][n], unhappy);
            }
        }
    }
    return f[r][c][n];
}

int a[11111];
int get_id(int i, int j, int c) {
    return i * c + j;
}
int task2(int r, int c, int n) {
    if ((r * c + 1) / 2 >= n)
        return 0;

    int nn = r * c - n;
    int ans1 = 2 * r * c - r - c;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            int id = get_id(i, j, c);
            a[id] = 0;
            if (i) a[id]++;
            if (j) a[id]++;
            if (i+1 < r) a[id]++;
            if (j+1 < c) a[id]++;
        }
    for (int adj = 4; adj >= 0; adj--) {
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++) {
                int id = get_id(i, j, c);
                if ((i + j) % 2 == 0 && nn > 0 && a[id] == adj) {
                    ans1 -= a[id];
                    a[id] = -1;
                    nn--;

                    if (i) a[get_id(i - 1, j, c)]--;
                    if (j) a[get_id(i, j - 1, c)]--;
                    if (i+1 < r) a[get_id(i + 1, j, c)]--;
                    if (j+1 < c) a[get_id(i, j + 1, c)]--;
                }
            }
    }

    nn = r * c - n;
    int ans2 = 2 * r * c - r - c;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            int id = get_id(i, j, c);
            a[id] = 0;
            if (i) a[id]++;
            if (j) a[id]++;
            if (i+1 < r) a[id]++;
            if (j+1 < c) a[id]++;
        }
    for (int adj = 4; adj >= 0; adj--) {
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++) {
                int id = get_id(i, j, c);
                if ((i + j) % 2 == 1 && nn > 0 && a[id] == adj) {
                    ans2 -= a[id];
                    a[id] = -1;
                    nn--;

                    if (i) a[get_id(i - 1, j, c)]--;
                    if (j) a[get_id(i, j - 1, c)]--;
                    if (i+1 < r) a[get_id(i + 1, j, c)]--;
                    if (j+1 < c) a[get_id(i, j + 1, c)]--;
                }
            }
    }

    return min(ans1, ans2);
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    memset(f, -1, sizeof f);

    int nTest;
    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {
        int r, c, n;
        scanf("%d%d%d", &r, &c, &n);
        printf("Case #%d: %d\n", test, task2(r, c, n));
    }

    return 0;
}
