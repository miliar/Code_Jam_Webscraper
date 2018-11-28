#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
#define fr(i, a, b) for (int i = (a); i < (b); i++)
#define all(c) (c).begin(), (c).end()
using namespace std;
typedef long long ll;
const ll inf = 1e9;
const ll mod = 1e9 + 7;

int dy[] = {1, 0, -1, 0};
int dx[] = {0, 1, 0, -1};

int main() {
    int cases;
    cin >> cases;

    rep (test, cases) {
        int h, w;
        cin >> h >> w;
        vector<string> G(h);
        vector<vector<int> > H(h, vector<int>(w));

        rep (i, h) {
            cin >> G[i];
            
            rep (j, w) {
                switch (G[i][j]) {
                    case 'v': H[i][j] = 0; break;
                    case '>': H[i][j] = 1; break;
                    case '^': H[i][j] = 2; break;
                    case '<': H[i][j] = 3; break;
                    default: H[i][j] = -1; break;
                }
            }
        }

        int ans = 0;
        bool ok = true;

        rep (i, h) {
            rep (j, w) {
                if (H[i][j] == -1) continue;

                bool dead = false;

                {
                    int y = i;
                    int x = j;
                    int dir = H[i][j];

                    for (;;) {
                        y += dy[dir];
                        x += dx[dir];

                        if (y < 0 || y >= h || x < 0 || x >= w) {
                            dead = true;
                            break;
                        }
                        
                        if (H[y][x] != -1) {
                            break;
                        }
                    }
                }

                if (!dead) continue;

                ans++;

                bool alive = false;

                rep (k, 4) {
                    int y = i;
                    int x = j;

                    for (;;) {
                        y += dy[k];
                        x += dx[k];

                        if (y < 0 || y >= h || x < 0 || x >= w) {
                            break;
                        }
                        
                        if (H[y][x] != -1) {
                            alive = true;
                            break;
                        }
                    }
                }

                if (!alive) ok = false;
            }
        }

        cout << "Case #" << test + 1 << ": ";

        if (ok) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
