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

int n, m;

struct State {
    int x, y, pos;
    State(int x, int y, int pos) : x(x), y(y), pos(pos) {}
};

const int MAXN = 20;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

bool used[MAXN][MAXN][4];

State toState(int k) {
    if (k < m) {
        return State(0, k, 0);
    }
    k -= m;
    if (k < n) {
        return State(k, m - 1, 1);
    }
    k -= n;
    if (k < m) {
        return State(n - 1, m - 1 - k, 2);
    }
    k -= m;
    return State(n - 1 - k, 0, 3);
}

bool validMove(int p1, int p2, char a) {
    if (p1 > p2) swap(p1, p2);
    if (p2 - p1 == 2) return false;
    if (a == 'f') {
        if (p1 == 0 && p2 == 1) return false;
        if (p1 == 2 && p2 == 3) return false;
        return true;
    }
    if (p1 == 0 && p2 == 3) return false;
    if (p1 == 1 && p2 == 2) return false;
    return true;
}

bool check(vector<int> p, vector<string> a) {
    queue<State> q;
    
    for (int i = 0; i < 2 * (n + m); i += 2) {
        State from = toState(p[i]);
        State to = toState(p[i + 1]);
        memset(used, 0, sizeof(used));
        used[from.x][from.y][from.pos] = true;
        q.push(from);
        while (!q.empty()) {
            State v = q.front(); q.pop();
            State u(v.x + dx[v.pos], v.y + dy[v.pos], (v.pos + 2) % 4);
            if (u.x >= 0 && u.x < n && u.y >= 0 && u.y < m && !used[u.x][u.y][u.pos]) {
                used[u.x][u.y][u.pos] = true;
                q.push(u);
            }
            
            forn(np, 4) {
                if (validMove(v.pos, np, a[v.x][v.y])) {
                    State u(v.x, v.y, np);
                    if (!used[u.x][u.y][u.pos]) {
                        used[u.x][u.y][u.pos] = true;
                        q.push(u);
                    }
                }
            }
        }
        
        if (!used[to.x][to.y][to.pos]) return false;
        
        forn(j, 2 * (n + m)) {
            if (j == i || j == i + 1) continue;
            State v = toState(p[j]);
            if (used[v.x][v.y][v.pos]) return false;
        }
     }
    return true;
}

void solveCase(int tc) {
    printf("Case #%d:\n", tc);
    cerr << tc << endl;
    cin >> n >> m;
    int k = 2 * (n + m);
    vector<int> p(k);
    forn(i, k) {
        cin >> p[i];
        p[i]--;
    }
    
    forn(mask, 1 << (n * m)) {
        vector<string> a(n, string(m, '.'));
        forn(i, n) {
            forn(j, m) {
                if (mask & (1 << (i * m + j))) a[i][j] = 'f'; else a[i][j] = 'b';
            }
        }
        
        if (check(p, a)) {
            forn(i, n) {
                forn(j, m) {
                    if (a[i][j] == 'f') cout << '/'; else cout << '\\';
                }
                cout << endl;
            }
            return;
        }
    }
    puts("IMPOSSIBLE");
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
