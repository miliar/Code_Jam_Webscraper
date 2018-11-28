#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>
#define MAXN 1010

int X1[MAXN], X2[MAXN], Y1[MAXN], Y2[MAXN];
int dist[MAXN][MAXN];

bool in(int l, int r, int x) {
    return l <= x && x <= r;
}

int dst(int l1, int r1, int l2, int r2) {
    if (in(l1, r1, l2) || in(l1, r1, r2) || in(l2, r2, l1) || in(l2, r2, r1))
        return -1;
    return min(min(abs(l1 - l2), abs(l1 - r2)), min(abs(r1 - l2), abs(r1 - r2))) - 1;
}

bool used[MAXN];
int ddist[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int w, h, b; 
        cin >> w >> h >> b;
        for (int i = 0; i < b; i++)
            cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
        for (int i = 0; i < b; i++) {
            dist[0][i + 1] = X1[i];
            dist[i + 1][b + 1] = w - 1 - X2[i];
        }
        dist[0][b + 1] = w;
        for (int i = 0; i < b; i++) {
            for (int j = 0; j < b; j++) {
                if (i == j) {
                    dist[i + 1][j + 1] = 0;
                    continue;
                }
                int xdist = dst(X1[i], X2[i], X1[j], X2[j]);
                int ydist = dst(Y1[i], Y2[i], Y1[j], Y2[j]);
                dist[i + 1][j + 1] = max(xdist, ydist);
            }
        }
        fill(used, used + b + 2, false);
        fill(ddist, ddist + b + 2, 1e+9);
        ddist[0] = 0;
        for (int i = 0; i < b + 2; i++) {
            int vv = -1;
            for (int i = 0; i < b + 2; i++) {
                if (used[i]) continue;
                if (vv == -1 || (ddist[vv] > ddist[i]))
                    vv = i;
            }
            if (vv == -1) break;
            used[vv] = true;
            for (int i = 0; i < b + 2; i++) {
                ddist[i] = min(ddist[i], ddist[vv] + dist[vv][i]);
            }
        }
        cout << "Case #" << i + 1 << ": " << ddist[b + 1] << endl;
    }
}
