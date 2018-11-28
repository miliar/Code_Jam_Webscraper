#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <iostream>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n )for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back

using namespace std;

int n, m;
int a[120][120];
int u[120], v[120];

bool solve() {
    forn(i, n) {
        u[i] = a[i][0];
        forn(j, m)
            u[i] = max(u[i], a[i][j]);
    }
    forn(j, m) {
        v[j] = a[0][j];
        forn(i, n)
            v[j] = max(v[j], a[i][j]);
    }
    forn(i, n)  forn(j, m)
        if( a[i][j] != min(u[i], v[j]) )
            return false;
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    fore(t, 1, T) {
        cin >> n >> m;
        forn(i, n) forn(j, m) cin >> a[i][j];
        cout << "Case #" << t << ": " << (solve() ? "YES" : "NO") << '\n';
    }
    return 0;
}
