#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())

using namespace std;
typedef long long LL;
typedef pair <int, int> pii;
const int MAXN = 105;

int t;

int get_dir(char ch) {
    if (ch == '>') {
        return 0;
    }
    if (ch == 'v') {
        return 1;
    }
    if (ch == '<') {
        return 2;
    }
    if (ch == '^') {
        return 3;
    }
    if (ch == '.') {
        return -1;
    }
    assert(false);
}

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int w, h;
int field[MAXN][MAXN];
string s; 

bool trygo(int x, int y, int dir) {
    int nowdir = dir;
    int posx = x;
    int posy = y;
    bool flag = false;
    while (true) {
        int nx = posx + dx[nowdir];
        int ny = posy + dy[nowdir];
        if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
            break;
        }
        if (field[nx][ny] != -1) {
            flag = true;
            break;
        }
        posx = nx;
        posy = ny;
    }
    return flag;
}

int main() {    
    //freopen(".in", "r", stdin);
    //freopen(".out", "w", stdout);

    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> h >> w;
        for (int j = 0; j < h; ++j) {
            cin >> s;
            for (int k = 0; k < w; ++k) {
                field[j][k] = get_dir(s[k]);
            }
        }

        bool gflag = false;
        int ans = 0;
        for (int j = 0; j < h; ++j) {
            for (int k = 0; k < w; ++k) {
                if (field[j][k] == -1) {
                    continue;
                }
                
                if (trygo(j, k, field[j][k])) {
                    continue;
                }

                bool flag = false;
                for (int d = 0; d < 4; ++d) {
                    if (d != field[j][k]) {
                        if (trygo(j, k, d)) {
                            flag = true;
                            break;
                        }
                    }
                }
                if (flag) {
                    ++ans;
                    continue;
                }
                gflag = true;
                break;
            }
            if (gflag) {
                break;
            }
        }
        if (gflag) {
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << ans << endl;
        }
    }

    return 0;
}