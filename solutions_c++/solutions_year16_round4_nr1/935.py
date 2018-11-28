#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxN = 20000;

int n, r, p, s, cnt, m;
int res[maxN], d[3];
int kq[maxN];

void Check(int i, int v, int s) {
    if (i >= m) return;
    if (d[v] <= 0) return;
    res[i] = v;
    if (i >= (1 << n)) {
        ++cnt;
        --d[v];
    }
    if (v == 0) {
        if ((n - s + 1) & 1) {
            Check(i + i, 0, s + 1);
            Check(i + i + 1, 2, s + 1);
        }
        else {
            Check(i + i, 2, s + 1);
            Check(i + i + 1, 0, s + 1);
        }
        return;
    }
    if (v == 1) {
        if ((n - s + 1) & 1) {
            Check(i + i, 0, s + 1);
            Check(i + i + 1, 1, s + 1);
        }
        else {
            Check(i + i, 1, s + 1);
            Check(i + i + 1, 0, s + 1);
        }
        return;
    }
    if (v == 2) {
        if ((n - s + 1) & 1) {
            Check(i + i, 2, s + 1);
            Check(i + i + 1, 1, s + 1);
        }
        else {
            Check(i + i, 1, s + 1);
            Check(i + i + 1, 2, s + 1);
        }
        return;
    }
}

bool Cmp(int i, int j, int len) {
    int pre = j;
    for(; i < pre; ++i, ++j) {
        if (res[i] != res[j]) {
            if ((res[i] == 2 && res[j] == 0) || (res[i] == 1 && (res[j] == 0 || res[j] == 2))) {
                    return true;
                }
        }
    }
    return false;
}

void Swap(int i, int j) {
    int pre = j;
    for(; i < pre; ++i, ++j) swap(res[i], res[j]);
}

void Sort() {
    for(int i = 0; i < n; ++i) {
        int st = (1 << n);
        while (st < (1 << (n + 1))) {
            int en = st + (1 << i);
            if (Cmp(st, en, (1 << i))) {
                Swap(st, en);
            }
            st = en + (1 << i);
        }
    }
}

void Update() {
    Sort();
    if (kq[(1 << n)] == 1000) {
        for(int i = (1 << n); i < (1 << (n + 1)); ++i)
            kq[i] = res[i];
    }
    else {
        bool ok = true;
        for(int i = (1 << n); i < (1 << (n + 1)); ++i) {
            if (kq[i] != res[i]) {
                if ((kq[i] == 2 && res[i] == 0) || (kq[i] == 1 && (res[i] == 0 || res[i] == 1))) {
                    ok = false;
                    break;
                }
            }
        }
        if (!ok) {
            for(int i = (1 << n); i < (1 << (n + 1)); ++i)
                kq[i] = res[i];
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int test = 1; test <= nTests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d %d %d %d", &n, &r, &p, &s);
        m = (1 << (n + 1));
        for(int i = 0; i <= m; ++i) kq[i] = 1000;
        cnt = 0;
        d[0] = p; d[1] = s; d[2] = r;
        bool ok = false;
        Check(1, 0, 1);
        if (cnt == (1 << n)) {
            ok = true;
            Update();
        }
        cnt = 0;
        d[0] = p; d[1] = s; d[2] = r;
        Check(1, 2, 1);
        if (cnt == (1 << n)) {
            ok = true;
            Update();
        }
        cnt = 0;
        d[0] = p; d[1] = s; d[2] = r;
        Check(1, 1, 1);
        if (cnt == (1 << n)) {
            ok = true;
            Update();
        }
        if (ok) {
            for(int i = (1 << n); i < (1 << (n + 1)); ++i) printf("%c", (kq[i] == 0 ? 'P' : kq[i] == 1 ? 'S' : 'R'));
            printf("\n");
        }
        else
        printf("IMPOSSIBLE\n");
    }

    return 0;
}
