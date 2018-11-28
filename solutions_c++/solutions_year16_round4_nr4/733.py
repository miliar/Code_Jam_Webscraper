#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int n, res, cnt;
int a[10][10], id[5], b[10][10];
bool mark[10];
vector <int> head;
bool ok;

void Check(int i) {
    if (i > n) return;
    bool y = false;
    if (!ok) return;
    for(int j = 1; j <= n; ++j) {
        if (!ok) return;
        if (a[id[i]][j] && !mark[j]) {
            y = true;
            mark[j] = true;
            Check(i + 1);
            mark[j] = false;
        }
    }
    if (!y) {
        ok = false;
        return;
    }
}

bool Check() {
    for(int i = 1; i <= n; ++i) id[i] = i;
    ok = true;
    do {
        if (!ok) break;
        memset(mark, false, sizeof mark);
        Check(1);
    } while (next_permutation(id + 1, id + n + 1));
    return ok;
}

void Update(int i, int j) {
    if (i > n) {
        if (Check()) {
            res = min(res, cnt);
        }
        return;
    }
    if (a[i][j] == 1) {
        if (j == n) Update(i + 1, 1);
        else Update(i, j + 1);
        return;
    }
    else {
        ++cnt;
        a[i][j] = 1;
        if (j == n) Update(i + 1, 1);
        else Update(i, j + 1);
        --cnt;
        a[i][j] = 0;
        if (j == n) Update(i + 1, 1);
        else Update(i, j + 1);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int test = 1; test <= nTests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d\n", &n);
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= n; ++j) {
                char ch; scanf("%c", &ch);
                a[i][j] = (ch - '0');
            }
            scanf("\n");
        }
        res = 100000;
        Update(1, 1);
        printf("%d\n", res);
    }

    return 0;
}

