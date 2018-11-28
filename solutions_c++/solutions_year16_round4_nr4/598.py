#include <bits/stdc++.h>
using namespace std;

int t, n;
int mat[4][4], ans, ex[4][4], arr[4];
bool used[4];

bool check2(int ind) {
    if (ind == n) return 1;
    bool ret = 1;
    int tot = 0;
    for (int i = 0; i < n; i++) {
        if (ex[arr[ind]][i] > 0 && !used[i]) {
            used[i] = 1;
            ret &= check2(ind + 1);
            used[i] = 0;
            tot++;
        }
    }
    ret &= (tot > 0);
    return ret;
}

bool check() {
    for (int i = 0; i < 4; i++) arr[i] = i;
    do {
        memset(used, 0, sizeof(used));
        if (!check2(0)) return 0;
    } while (next_permutation(arr, arr + n));
    return 1;
}

int main(void) {
    if (fopen("d-small.in", "r")) {
        freopen("d-small.in", "r", stdin);
        freopen("d-small.out", "w", stdout);
    }
    if (fopen("d-large.in", "r")) {
        freopen("d-large.in", "r", stdin);
        freopen("d-large.out", "w", stdout);
    }
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        ans = 16;
        cin >> n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char c;
                cin >> c;
                mat[i][j] = c - '0';
            }
        }
        for (int i = 0; i < (1 << (n * n)); i++) {
            int val = 0;
            bool bad = 0;
            for (int j = 0; j < n && !bad; j++) {
                for (int k = 0; k < n && !bad; k++) {
                    ex[j][k] = ((i >> (j * n + k)) & 1);
                    if (ex[j][k] == 0 && mat[j][k] == 1) bad = 1;
                    else if (ex[j][k] != mat[j][k]) val++;
                    if (val > ans) bad = 1;
                }
            }
            if (!bad && check() && val < ans) {
                ans = min(ans, val);
            }
        }
        printf("Case #%d: %d\n", ii, ans);
    }
    return 0;
}
