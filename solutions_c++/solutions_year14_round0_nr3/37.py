#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

#define TWO(x) (1<<(x))
#define CONTAIN(S,x) (S & TWO(x))
;

char a[55][55], tmp[55][55];
int m, n, k;
bool hasSolution;

void solve1() {
    int nFree = m*n - k;
    hasSolution = true;
    FOR(i,1,n) {
        if (i == 1) a[1][i] = 'c';
        else if (i <= nFree) a[1][i] = '.';
        else a[1][i] = '*';
    }
}

void solve2() {
    int nFree = m*n - k;
    if (nFree == 1) {
        hasSolution = true;
        FOR(i,1,m) FOR(j,1,n) {
            if (i == 1 && j == 1) a[i][j] = 'c';
            else a[i][j] = '*';
        }
    }
    else if (nFree % 2 == 0 && nFree != 2) {
        hasSolution = true;
        FOR(i,1,m) FOR(j,1,n) {
            if (i == 1 && j == 1) a[i][j] = 'c';
            else if (j <= nFree / 2) a[i][j] = '.';
            else a[i][j] = '*';
        }
    }
}

void full(int nFull, int rem) {
    FOR(i,1,m) FOR(j,1,n) {
        if (i == 1 && j == 1) a[i][j] = 'c';
        else if (i <= nFull) a[i][j] = '.';
        else if (i == nFull + 1 && j <= rem) a[i][j] = '.';
        else a[i][j] = '*';
    }
}

void solve() {
    int nFree = m*n - k;
    if (nFree == 1) {
        hasSolution = true;
        full(0, 1);
    }
    else if (n % 2 == 0) {
        if (nFree >= 4 && nFree % 2 == 0) {
            hasSolution = true;
            if (nFree <= 2*n) {
                FOR(i,1,m) FOR(j,1,n) {
                    if (i == 1 && j == 1) a[i][j] = 'c';
                    else if (i <= 2 && j <= nFree / 2) a[i][j] = '.';
                    else a[i][j] = '*';
                }
            }
            else {
                full(nFree / n, nFree % n);
            }
        }
        else if (nFree >= 9 && nFree % 2 == 1) {
            hasSolution = true;
            if (nFree <= 2*n + 3) {
                FOR(i,1,m) FOR(j,1,n) {
                    if (i == 1 && j == 1) a[i][j] = 'c';
                    else if (i <= 3 && j <= 3) a[i][j] = '.';
                    else if (i <= 2 && j <= 3 + (nFree - 9) / 2) a[i][j] = '.';
                    else a[i][j] = '*';
                }
            }
            else {
                if (nFree % n != 1) {
                    full(nFree / n, nFree % n);
                }
                else {
                    int nFull = nFree / n;
                    FOR(i,1,m) FOR(j,1,n) {
                        if (i == 1 && j == 1) a[i][j] = 'c';
                        else if (i <= nFull - 1) a[i][j] = '.';
                        else if (i <= nFull && j < n) a[i][j] = '.';
                        else if (i <= nFull+1 && j <= 2) a[i][j] = '.';
                        else a[i][j] = '*';
                    }
                }
            }
        }
    }
    else { // n % 2 == 1
        if (nFree % n != 1 && nFree >= 2 * n) {
            hasSolution = true;
            full(nFree / n, nFree % n);
        }
        else if (nFree % 2 == 0 && nFree <= 2*n && nFree >= 4) {
            hasSolution = true;
            FOR(i,1,m) FOR(j,1,n) {
                if (i == 1 && j == 1) a[i][j] = 'c';
                else if (i <= 2 && j <= nFree / 2) a[i][j] = '.';
                else a[i][j] = '*';
            }
        }
        else if (nFree % 2 == 1 && nFree <= 2*n+3 && nFree >= 9) {
            hasSolution = true;
            FOR(i,1,m) FOR(j,1,n) {
                if (i == 1 && j == 1) a[i][j] = 'c';
                else if (i <= 3 && j <= 3) a[i][j] = '.';
                else if (i <= 2 && j <= 3 + (nFree - 9) / 2) a[i][j] = '.';
                else a[i][j] = '*';
            }
        }
        else {
            FOR(u,1,m) if (k % u == 0) {
                int v = k / u;
                if (v <= n && v != n-1 && u != m-1) {
                    hasSolution = true;
                    FOR(i,1,m) FOR(j,1,n) {
                        if (i == 1 && j == 1) a[i][j] = 'c';
                        else if (i >= m-u+1 && j >= n-v+1) a[i][j] = '*';
                        else a[i][j] = '.';
                    }
                    break;
                }
            }
        }
    }
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> m >> n >> k;
        cout << "Case #" << test << ":\n";
        hasSolution = false;
        bool swapped = false;
        if (m > n) {
            swapped = true;
            swap(m, n);
        }

        if (m == 1) solve1();
        else if (m == 2) solve2();
        else solve();

        if (swapped) {
            swap(m, n);
            FOR(i,1,m) FOR(j,1,n) tmp[i][j] = a[j][i];
            FOR(i,1,m) FOR(j,1,n) a[i][j] = tmp[i][j];
        }
        if (hasSolution) {
            FOR(i,1,m) FOR(j,1,n) {
                cout << a[i][j];
                if (j == n) cout << endl;
            }
        }
        else {
            cout << "Impossible\n";
        }
    }
    return 0;
}
