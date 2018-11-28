#include <iostream>
#include <cstring>
#include <stdexcept>
#include <vector>
#include <algorithm>

using namespace std;

char s[103][103];
bool used[103][103][4];

const int INF = 0x7f7f7f7f;

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

int r, c;

int getdir(char op) {
    if (op == '>') return 0;
    if (op == 'v') return 1;
    if (op == '<') return 2;
    if (op == '^') return 3;
    throw logic_error("Unknown op");
}

char opposite(char op) {
    if (op == '>') return '<';
    if (op == 'v') return '^';
    if (op == '<') return '>';
    if (op == '^') return 'v';
    throw logic_error("Unknown op");
}

int run(int x, int y) {
    if (s[x][y] == '.') return 0;
    int curdir = getdir(s[x][y]);
    cerr << "running " << x << ' ' << y << " with curdir = " << curdir << endl;

    for (;;) {
        x += dx[curdir];
        y += dy[curdir];

        if (x < 0 || y < 0 || x >= r || y >= c) {
            return 1;
        }

        if (s[x][y] != '.') return 0;
    }
}

void solve(int e) {
    cin >> r >> c;

    for (int i=0; i<r; ++i)
        cin >> s[i];

    cout << "Case #" << e << ": ";
    int ans = 0;
    for (int i=0; i<r; ++i) {
        for (int u=0; u<c; ++u) {
            memset(used, 0, sizeof used);

            int add = run(i, u);
            if (add) {
                ++ans;
                cerr << "bad arrow is " << i << ' ' << u << endl;
                bool done = false;
                for (const char change : {'>', '<', 'v', '^'}) {
                    memset(used, 0, sizeof used);
                    s[i][u] = change;

                    add = run(i, u);

                    if (add == 0) {
                        cerr << "Everything is ok if we change it to " << change << endl;
                        done = true;
                        break;
                    }
                }

                if (!done) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
            }
        }
    }

    cout << ans << endl;
}

int main() {
    int t; cin >> t;
    for (int e=1; e<=t; ++e)
        solve(e);

    return 0;
}



