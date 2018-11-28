#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
#include <cassert>
using namespace std;

pair<pair<int, int>, int> to_pos(int ix, int w, int h)
{
    if (ix < w) return make_pair(make_pair(ix, 0), 2);
    ix -= w;
    if (ix < h) return make_pair(make_pair(w - 1, ix), 3);
    ix -= h;
    if (ix < w) return make_pair(make_pair(w - 1 - ix, h - 1), 0);
    ix -= w;
    return make_pair(make_pair(0, h - 1 - ix), 1);
}

int to_ix(int x, int y, int w, int h)
{
    if (y < 0) return x;
    if (x >= w) return w + y;
    if (y >= h) return w + h + w - 1 - x;
    return w + h + w + h - 1 - y;
}

void solve()
{
    cout << endl;

    const static int vect[4][2] = {
        {0, -1}, {1, 0}, {0, 1}, {-1, 0}
    };

    int h, w; cin >> h >> w;
    vector<int> ps((h + w) * 2);

    for (int i = 0; i < (h + w) * 2; i+=2) {
        int a, b; cin >> a >> b;
        a--, b--;
        ps[a] = b;
        ps[b] = a;
    }

    for (int b = 0; b < (1 << (h * w)); b++) {
        bool ok = true;

        for (int cc = 0; cc < (h + w) * 2; cc++) {
            auto ttt = to_pos(cc, w, h);
            int cx = ttt.first.first;
            int cy = ttt.first.second;
            int dir = ttt.second;

            while (cx >= 0 && cx < w && cy >= 0 && cy < h) {
                if (b & (1 << (cx + cy * w))) {
                    dir = dir ^ 1;
                } else {
                    dir = dir ^ 3;
                }

                cx += vect[dir][0];
                cy += vect[dir][1];
            }

            int dd = to_ix(cx, cy, w, h);

            // cout << cc << ", " << dd << endl;

            ok &= ps[cc] == dd && ps[dd] == cc;
            if (!ok) break;
        }

        if (ok) {
            for (int y = 0; y < h; y++) {
                for (int x = 0; x < w; x++) {
                    cout << ((b & (1 << (x + y * w)))? '/' : '\\');
                }
                cout << endl;
            }

            return;
        }
    }

    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    int t; cin >> t;
    for (int cn = 1; cn <= t; cn++) {
        cout << "Case #" << cn << ":";
        solve();
    }

    return 0;
}
