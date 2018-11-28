#include <cstdio>

#define forn(i, n) for (int i = 0; i < (n); i++)

int n, m;
int a[128][128];

bool go() {
    forn(i, n) forn(j, m) {
        bool o1 = true, o2 = true;
        forn(k, n) o1 &= (a[k][j] <= a[i][j]);
        forn(k, m) o2 &= (a[i][k] <= a[i][j]);
        if (!o1 && !o2) return false;
    }
    return true;
}

int main() {
    int __;
    scanf("%d", &__);
    forn(_, __) {
        scanf("%d%d", &n, &m);
        forn(i, n) forn(j, m) scanf("%d", &a[i][j]);
        printf("Case #%d: %s\n", _+1, go() ? "YES" : "NO");
    }
    return 0;
}

