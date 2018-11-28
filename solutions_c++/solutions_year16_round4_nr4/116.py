#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define pb push_back

int n;
vector<bool> used;
vector<int> mm;

bool go(int v, const vector< vector<bool> >& g, const vector<bool>& av) {
    if (used[v]) return false;
    used[v] = true;
    
    forn(u, n) {
        if (av[u] && g[v][u]) {
            if (mm[u] == -1 || go(mm[u], g, av)) {
                mm[u] = v;
                return true;
            }
        }
    }
    
    return false;
}

bool check(vector< vector<bool> > g) {
    forn(i, n) {
        int size = 0;
        mm = vector<int>(n, -1);
        forn(j, n) {
            if (i == j) continue;
            used = vector<bool>(n);
            if (go(j, g, g[i])) {
                size++;
            }
        }
        int cnt = 0;
        forn(j, n) if (g[i][j]) cnt++;
        if (cnt == size) return false;
    }
    return true;
}

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;

    cin >> n;
    vector<string> a(n);
    forn(i, n) cin >> a[i];
    int best = 10000;
    forn(mask, 1 << (n * n)) {
        vector< vector<bool> > g(n, vector<bool>(n));
        int b = 0;
        int cost = 0;
        forn(i, n) {
            forn(j, n) {
                int e = (mask >> b) & 1;
                b++;
                if (e == 0 && a[i][j] == '1') {
                    cost = -1;
                    break;
                }
                g[i][j] = e;
                if (e == 1 && a[i][j] == '0') {
                    cost++;
                }
            }
            if (cost == -1) break;
        }
        if (cost != -1 && check(g) && best > cost) {
            best = cost;
        }
    }
    cout << best << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
