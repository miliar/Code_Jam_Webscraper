#include <bits/stdc++.h>
using namespace std;

const int ci[] = {0, 1, 0, -1, 0};
const int cj[] = {0, 0, -1, 0, 1};

int n_test;
int r, c;
char a[111][111];
bool ok[111][111][5];

bool inside(int i, int j) {
    return i >= 1 && j >= 1 && i <= r && j <= c;
}

bool check_dir(int i, int j, int d) {
    int ii = i + ci[d];
    int jj = j + cj[d];

    while (inside(ii, jj) && a[ii][jj] == 0) {
        ii += ci[d];
        jj += cj[d];
    }

    return inside(ii, jj);
}

int main() {

    // freopen("A.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    scanf("%d", &n_test);
    for (int test = 1; test <= n_test; test++) {
        scanf("%d%d", &r, &c);

        memset(ok, 1, sizeof ok);
        for (int i = 1; i <= r; i++) {
            scanf("%s", a[i] + 1);
            for (int j = 1; j <= c; j++)
                if (a[i][j] == '.')
                    a[i][j] = 0;
                else if (a[i][j] == 'v')
                    a[i][j] = 1;
                else if (a[i][j] == '<')
                    a[i][j] = 2;
                else if (a[i][j] == '^')
                    a[i][j] = 3;
                else if (a[i][j] == '>')
                    a[i][j] = 4;
        }

        int ret = 0;
        for (int i = 1; i <= r && ret >= 0; i++)
            for (int j = 1; j <= c && ret >= 0; j++) {
                if (a[i][j] == 0) 
                    continue;
                if (!check_dir(i, j, a[i][j])) {
                    bool ok = false;
                    for (int d = 1; d < 5; d++)
                        if (d != a[i][j])
                            if (check_dir(i, j, d)) {
                                a[i][j] = d;
                                ok = true;
                                break;
                            }

                    if (ok)
                        ret++;
                    else
                        ret = -1e9;
                }
            }

        if (ret >= 0) printf("Case #%d: %d\n", test, ret);
        else printf("Case #%d: IMPOSSIBLE\n", test);
    }

    return 0;
}